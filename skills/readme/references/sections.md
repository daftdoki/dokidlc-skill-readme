# Sections of a README, for the reader who wants to use the software

The reader is a person deciding whether to use this, then getting it to run once. Contributors and maintainers get one line and a link. A repository that is an agent's home rather than software has its own adjustments in `agent-home.md`. `readme-check` runs the mechanical checks; this file holds the rules a script cannot apply. The research behind it is `docs/research/readme-for-users.md` in the agent-builder repository.

## The reader's questions, in order

1. What is this? (title, one-liner)
2. Does it solve my problem, and why this one over the alternatives? (description, why)
3. What does it look like when it runs? (usage example, screenshot if there is a UI)
4. Can I use it? (license, platform, prerequisites, status)
5. How do I get it running once? (install, first run)
6. What will bite me? (caveats)
7. Where is the rest, and where do I ask? (other docs, support)

Sections follow this order, with one exception: a permissive license sits last because it disqualifies nobody. The order is set by how fast a reader can bail. A reader who learns in line 2 that this is not for them has lost ten seconds; one who learns it under "Supported platforms" at line 90 has lost the install.

## Section table

R is required, C is conditional on the stated condition, O is optional for this reader.

| Section | Reader's question | Status | Create rule | Judgment check |
|---|---|---|---|---|
| Title | What is this called? | R | First heading is the project name. If it differs from the repository or package name, the description says why. | The name is self-evident, or the one-liner rescues it. |
| One-liner | What does it do? | R | One sentence under 120 characters, directly under the title, no heading. Same text as the GitHub description and the package description field. | Names the outcome for the reader, not the stack. Defines any term the name assumes. Could not be pasted into another project's README unchanged. |
| Description | Does it solve my problem? | R | Prose first: one or two paragraphs that say what the parts are, which of them stand alone, and how they connect. A reader who could run one part without the others learns that here. Then the capabilities, each a full sentence with the detail to picture it, covering every entry point. Second person, active voice. | Reads like a person explaining the project, not a feature list. Each part a reader can deploy on its own is named. Each capability is one the reader can verify by running it. A capability that lets the reader make something of their own (a theme, a script against the API) outranks one that shows them something. How the code is organised comes after the purpose, if at all. |
| Why | Why this over the alternatives? | R | One paragraph: the problem it exists for and where it differs from the nearest alternative. An origin story serves a new project. If no alternative exists, one sentence says so. | The reader can tell what it is not for. Present in 25.7% of READMEs sampled by Prana et al., so its absence is the common defect. |
| Visuals | What does it look like? | C: a UI, a display, or visual output | Screenshot or short GIF near the top, stored in the repository, with alt text. | The text beside the image says what the image shows. Deleting every image loses no fact. |
| License | May I use it? | R | SPDX identifier, owner, link to `LICENSE`. Permissive at the end. A non-permissive license or a use restriction gets a one-line note under the description as well. | Placement matches how surprising the license is. |
| Status | Is this alive, and is it stable? | R | One line: stable, experimental, maintained, or deprecated. Version and supported platforms when they change the answer. | The reader can tell whether to build on it. Present in 21.4% of sampled READMEs; the most commonly missing answer. |
| Prerequisites | What do I need first? | C: anything beyond the language's standard install | List with versions, before install. Link each prerequisite's own install page. | Nothing out of scope is explained, only named. |
| Install | How do I get it? | R | One code block. The standard package-manager command even when obvious; new users of the ecosystem exist. System-specific notes as sub-bullets. | The commands work on a clean machine. Run them if you can. |
| Usage | How do I run it once? | R | One runnable example with its output. CLI: the invocation and what it prints. Library: the import and one call. Stop when the project has worked once. Keep the example as a file in the repository. | The example is the common case. The reader copies it and edits at most a path. Walkthroughs live elsewhere. |
| Caveats | What will bite me? | R | Short list. If a caveat disqualifies, it goes before install. | Every sharp edge a first-time user hits is named. |
| Configuration | How do I change its behavior? | C: the project reads config | Where the config lives and the two or three settings a first run may need. | Full option tables are absent. |
| API | What does it expose? | C: a library | Signatures, parameter types, defaults, return values, caveats. A single link to generated reference is enough. | Optional parameters and their defaults are marked. An application has no API section. |
| Other docs | Where is the rest? | R | A list of links, each with one clause saying what the target holds: the docs directory, wiki, site, man page, and the companion files. | Each link has a description. A README that is the only documentation says so. |
| Support | Where do I ask? | R | Where to file a bug and where to ask a question. If unsupported, say so. | The reader knows whether to expect an answer. |
| Contributing, maintainers, thanks, roadmap | May I help, who runs this? | O | One line and a link to `CONTRIBUTING.md`. Whether PRs are accepted. Roadmap only when the reader's decision depends on a planned feature. | The contributor process is not inlined. |
| Table of contents | Where in this file? | O | None on GitHub, which generates one from the headings. Add one only when the file renders elsewhere and is long. | Absent unless justified. |
| Badges | Is it healthy? | O | Each badge answers a question this reader has: version, license. Newline delimited, no heading. | A build-status badge is a signal for maintainers and belongs in their inbox. |

## What stays out

The grader flags these; the writer moves them to the document that owns them and leaves a one-line pointer.

- Development process, coding standards, test commands, branch rules. `CONTRIBUTING.md` or `docs/`.
- Internals: how the code inside a part is organised, its modules, layers, and threads. `docs/architecture.md`. The parts themselves, and which of them stand alone, are not internals; they are what the reader deploys, and they belong in the description.
- Research provenance: verification dates, "verified", "assumed", citations to captures or sessions. The README says what the tool does and what to type.
- Changelog and version history. `CHANGELOG.md`.
- Full option and API reference. The README shows what the first run needs.
- Extended tutorials. Stop once the project works once.
- Images that carry facts nothing else states. The repository outlives the image host.
- Adjectives. "Fast", "powerful", "simple". Replace each with the number or the mechanism.

## Decisions

Four places the sources disagree, settled here so every run lands the same way.

- Order: the reader's questions above, install before usage, API after usage.
- Length: short. Soft ceiling 150 lines. A section that passes a few paragraphs moves to `docs/` with a one-line pointer. Published package READMEs run a median of 85 lines.
- License placement: last when permissive; also a note near the top when not.
- Badges: a few, each justified. Build status is noise for this reader.

## Facts about GitHub

- GitHub generates a table of contents from the headings.
- Relative links and image paths work and follow the branch. Link `docs/` and `LICENSE` relatively.
- GitHub surfaces the license, citation file, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` in its own UI. The README links them and does not restate them.
- The README is picked up from `.github/`, the root, or `docs/`, in that priority. Keep one, at the root.
