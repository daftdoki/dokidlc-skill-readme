---
name: readme
description: Write, grade, or keep a README.md for the person deciding whether to use the software. Use when asked to write or rewrite a README, when asked whether a README is any good, and when a change lands and someone asks whether the README needs to move.
---

# README

A README is the reader's first look and often the only one. Its job is to let a person decide, fast, whether this software solves their problem, and then get it running once. Everything else is a link. The reader in scope is a user. Contributors, maintainers, and the project's own developers get one line each.

`readme-check`, on PATH while this plugin is enabled, runs the mechanical checks: title, one-liner, install and usage code blocks, license, links, length, the two gates, and the `unslop` patterns a regex can find (vocabulary, filler, curly quotes, em dashes, emoji, bold-label bullets). It exits 1 on a failed gate or required check. `readme-check --json` for machine output, `--network` to also test http links, `--no-code` for a repository with no software in it. The checks a script cannot make are in `references/sections.md`; read it before you write or grade.

Two facts drive the weighting. Prana et al. hand-labelled 4,226 README sections: almost every README says what the project is and how to install it, but only 25.7% say why it exists and 21.4% say whether it is alive. Those two are the gates. A README that fails a gate fails, whatever else it does well.

Three verbs. Pick the one the request names.

## Write

Creates a README or rewrites one. The old README is a source of facts, never of structure.

1. Read `references/sections.md`. If the repository holds no software, only a `CLAUDE.md`, skills, and settings that a person opens in Claude Code, read `references/agent-home.md` as well.
2. Learn the project from the environment: the package manifest, `--help` output, entry points, `docs/`, tests, `LICENSE`, the git remote. Inventory every entry point before you write a word: each console script, subcommand, service, and API. A repository's name often names one part, and the README covers the set. Collect, in this order, the name, the one-liner, the parts and which of them stand alone, the capabilities a reader can verify, the nearest alternative, the runtime and its version, the install command, the first-run command and what it prints, the caveats, the config a first run needs, the documents worth linking, where to ask, the license, and the status.
3. Run the install and first-run commands when the environment allows. Paste real output. Where a fact is out of reach (status, alternatives, output you could not produce), ask the creator once, listing every missing fact in one question. An invented status or a guessed output is worse than a gap.
4. Write the file in the section order of the reference. The description is prose before it is a list: say what the parts are and how they fit, then the capabilities as sentences with the detail a reader needs to picture them. A bullet short enough to be a heading is too short. Each capability states something the reader can check by running the software; a line that fits another project unchanged says nothing about this one.
5. Invoke the `unslop` skill on the draft. The checker catches its mechanical patterns; the skill catches puffery, rhythm, and mannered prose, which no regex does. Where the skill is not installed, say so in the report and go on.
6. Run `readme-check`. Fix every FAIL. For each WARN, fix it or say in your report why it stands.
7. Read the result once as the reader, asking the seven questions in order. Each must be answered by the line where the reader expects it.

Done when `readme-check` exits 0 and every one of the seven questions has its line. Report what you wrote, what you could not learn, and every WARN you left.

## Grade

Reports on an existing README. Writes nothing to the repository.

1. Read `references/sections.md`, and `references/agent-home.md` if the repository is an agent's home rather than software.
2. Run `readme-check`.
3. Give every row of the section table a verdict: pass, fail, or waived because the condition is not met. Apply the judgment column, not only the script's line. The script finds a heading called "Why"; you decide whether the paragraph under it tells the reader what this is not for.
4. Walk the "what stays out" list and name each defect with its line.
5. For polish, invoke the `unslop` skill on the file and keep what it finds, by line. The checker's voice class is the mechanical subset; the skill is the rest.

Report in this order: gates, required sections missing or failing, material to move out, polish. Each finding names the line and the fix in one sentence. End with the reader's verdict in one line: can a person decide from this file, and can they run it once.

Done when every row has a verdict and every leave-out defect is named.

## Diff

Answers whether a change needs a README edit. There is no file-level trigger for README drift; a README moves when what the project does moves, and only reading the change tells you that.

1. Read the change: `git diff --stat RANGE`, then the diff of anything that touches entry points, CLI arguments, configuration, install files, supported platforms, the license, or `docs/`.
2. Read the README's headings and its install, usage, caveats, and status lines.
3. For each change a user could notice, name the README section that moves and the edit in one sentence. For each change they could not, say "internal" and why.

A user notices a change to what the project does, how it installs, how it first runs, the config a first run needs, the platforms it supports, its license, its status, or its caveats. A user does not notice a refactor, a test, a dependency bump that changes no command, or a document under `docs/` the README already links.

Done when every changed behavior is matched to a section or declared internal. Report the list; make the edits only when asked.
