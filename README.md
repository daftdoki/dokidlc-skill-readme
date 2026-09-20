# dokidlc-skill-readme

A Claude Code plugin that writes and grades a README.md for the person deciding whether to use the software.

It carries one skill, `readme`, with three verbs. Write creates or rewrites a README from what the repository holds. Grade reports on an existing one, ordered by what fails the reader first. Diff reads a commit range and says which README line moves, or why none does. A checker, `readme-check`, runs the mechanical part: title, one-liner, install and usage blocks, license, links, length, and two gates.

## Why the two gates

Most READMEs say what the project is and how to install it. Few say why it exists rather than the alternatives, and fewer say whether it is alive. Prana et al. hand-labelled 4,226 README sections and found the why in 25.7% of files and the status in 21.4%. Those are the two answers a user needs to decide, so a README that lacks either fails the check whatever else it does well. Other README guides list sections; this one weights them by how fast a reader can bail.

Status: experimental. Built 2026-09-20 for the agents under the dokidlc marketplace, and used on their own repositories first.

## Install

From the dokidlc marketplace, once per machine:

```
claude plugin install readme@dokidlc
```

Claude Code puts `readme-check` on PATH while the plugin is enabled. It needs Python 3.12 or later and nothing else.

## Run it

Ask the agent to write, grade, or check a README, or run the checker yourself from a repository root:

```
readme-check
```

It prints one line per check and exits 1 when a gate or a required check fails:

```
PASS required    title: "ch-display" matches the project name
FAIL gate        why: nothing says why this exists rather than the alternatives
FAIL gate        status: nothing says whether this is stable, experimental, or maintained
PASS required    install: "Install" has a code block
```

`readme-check --json` for machine output, `--network` to also test http links, and `--no-code` for a repository with no software in it.

## Caveats

The checker matches headings and phrases, so it can miss a why that is written without the word and pass a status line that says nothing. The skill's judgment pass, not the script, is the grade. The checker does not know whether the project has a UI, so it only hints at a missing screenshot when the repository holds HTML.

## Other docs

- [skills/readme/SKILL.md](skills/readme/SKILL.md) is the skill: the three verbs and their steps.
- [skills/readme/references/sections.md](skills/readme/references/sections.md) is the section table, the leave-out list, and the decisions the skill runs on.
- The research behind the table is `docs/research/readme-for-users.md` in the [agent-builder](https://github.com/daftdoki/agent-builder) repository.

Questions and bugs go to the [issue tracker](https://github.com/daftdoki/dokidlc-skill-readme/issues).

## License

MIT, DaftDoki. See [LICENSE](LICENSE).
