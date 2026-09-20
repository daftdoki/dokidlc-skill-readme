import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "bin" / "readme-check"

GOOD = """# widget

Turns a CSV of readings into one PNG per day.

Why this and not a spreadsheet: it runs unattended and never asks about date formats. Status: stable, used nightly since 2025.

## Install

```
pip install widget
```

## Usage

```
widget readings.csv
```

It prints one line per file written:

```
wrote 2026-09-20.png
```

Caveat: it does not read Excel files.

Bugs go to the [issue tracker](https://example.com/widget/issues).

## License

MIT. See [LICENSE](LICENSE).
"""


def run(path: Path, *args: str) -> tuple[int, list[dict]]:
    out = subprocess.run(
        [sys.executable, str(CHECK), str(path), "--json", *args],
        capture_output=True, text=True,
    )
    return out.returncode, json.loads(out.stdout)


def repo(tmp_path: Path, readme: str, license: bool = True) -> Path:
    (tmp_path / "README.md").write_text(readme)
    if license:
        (tmp_path / "LICENSE").write_text("MIT License\n")
    return tmp_path


def verdicts(findings: list[dict], check: str) -> set[str]:
    return {f["verdict"] for f in findings if f["check"] == check}


def test_own_readme_passes():
    code, findings = run(ROOT)
    assert code == 0, [f for f in findings if f["verdict"] == "FAIL"]


def test_good_fixture_is_clean(tmp_path):
    (tmp_path / "widget").mkdir()
    code, findings = run(repo(tmp_path / "widget", GOOD))
    assert code == 0
    assert not [f for f in findings if f["verdict"] in ("FAIL", "WARN")], findings


def test_missing_gates_fail(tmp_path):
    text = GOOD.replace("Why this and not a spreadsheet: it runs unattended and never asks about date formats. Status: stable, used nightly since 2025.\n", "")
    code, findings = run(repo(tmp_path, text))
    assert code == 1
    assert verdicts(findings, "why") == {"FAIL"}
    assert verdicts(findings, "status") == {"FAIL"}


def test_missing_readme(tmp_path):
    code, findings = run(tmp_path)
    assert code == 1 and findings[0]["check"] == "readme"


def test_broken_relative_link_fails(tmp_path):
    code, findings = run(repo(tmp_path, GOOD.replace("[LICENSE](LICENSE)", "[LICENSE](LICENSE.txt)")))
    assert verdicts(findings, "links") == {"FAIL"}


def test_headings_inside_fences_are_ignored(tmp_path):
    text = GOOD.replace("```\nwidget readings.csv\n```", "```\n# not a heading\nwidget readings.csv\n```")
    code, findings = run(repo(tmp_path, text))
    assert not [f for f in findings if f["check"] == "headings"]


def test_no_code_waives_install_and_usage(tmp_path):
    text = "# notes\n\nA list of what I read.\n\nWhy: nothing else keeps them. Status: maintained.\n\n## License\n\nMIT. See [LICENSE](LICENSE).\n"
    code, findings = run(repo(tmp_path, text), "--no-code")
    assert verdicts(findings, "install") == {"INFO"}
    assert verdicts(findings, "usage") == {"INFO"}


def test_adjectives_in_code_and_alt_text_are_not_counted(tmp_path):
    (tmp_path / "simple.png").write_bytes(b"")
    text = GOOD.replace("Turns a CSV", "The `simple` theme ![simple](simple.png) turns a CSV")
    code, findings = run(repo(tmp_path, text))
    assert not verdicts(findings, "vocabulary")


def test_adjectives_in_prose_warn(tmp_path):
    code, findings = run(repo(tmp_path, GOOD.replace("Turns a CSV", "A blazing fast tool that turns a CSV")))
    assert verdicts(findings, "vocabulary") == {"WARN"}


def test_non_permissive_license_far_down_warns(tmp_path):
    text = GOOD.replace("MIT. See", "GPL-3.0. See")
    text = text.replace("## License", "\n" * 40 + "## License")
    code, findings = run(repo(tmp_path, text))
    assert "WARN" in verdicts(findings, "license")


def test_docs_dir_unlinked_fails(tmp_path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text("# guide\n")
    code, findings = run(repo(tmp_path, GOOD))
    assert verdicts(findings, "other-docs") == {"FAIL"}


def test_long_readme_warns(tmp_path):
    text = GOOD.replace("## License", "## Notes\n\n" + "line\n" * 160 + "\n## License")
    code, findings = run(repo(tmp_path, text))
    assert "WARN" in verdicts(findings, "length")


def test_title_case_heading_warns(tmp_path):
    code, findings = run(repo(tmp_path, GOOD.replace("## Usage", "## Getting Started Quickly")))
    assert "WARN" in verdicts(findings, "headings")


@pytest.mark.parametrize("bad", ["one PNG \u2014 per day", "one \u201cPNG\u201d per day"])
def test_em_dash_and_curly_quotes_warn(tmp_path, bad):
    code, findings = run(repo(tmp_path, GOOD.replace("one PNG per day", bad)))
    assert verdicts(findings, "punctuation") == {"WARN"}


def test_filler_and_vocabulary_warn(tmp_path):
    text = GOOD.replace("Turns a CSV", "In order to leverage your readings, it turns a CSV")
    code, findings = run(repo(tmp_path, text))
    assert verdicts(findings, "filler") == {"WARN"}
    assert verdicts(findings, "vocabulary") == {"WARN"}


def test_inline_header_bullets_warn(tmp_path):
    bullets = "\n".join(f"- **Item {i}:** item {i} does a thing." for i in range(3))
    text = GOOD.replace("Caveat: it does not read Excel files.", "Caveat: it does not read Excel files.\n\n" + bullets)
    code, findings = run(repo(tmp_path, text))
    assert verdicts(findings, "inline-headers") == {"WARN"}


def test_emoji_in_heading_warns(tmp_path):
    code, findings = run(repo(tmp_path, GOOD.replace("## Usage", "## Usage \U0001F680")))
    assert verdicts(findings, "emoji") == {"WARN"}


def test_bare_why_is_not_a_why(tmp_path):
    text = GOOD.replace("Why this and not a spreadsheet: it runs unattended and never asks about date formats.", "The docs say why.")
    code, findings = run(repo(tmp_path, text))
    assert verdicts(findings, "why") == {"FAIL"}


def test_agent_home_missing_license_warns(tmp_path):
    (tmp_path / "CLAUDE.md").write_text("# rules\n")
    text = GOOD.replace("MIT. See [LICENSE](LICENSE).", "None declared.")
    code, findings = run(repo(tmp_path, text, license=False))
    assert verdicts(findings, "agent-home") == {"INFO"}
    assert "FAIL" not in verdicts(findings, "license")
