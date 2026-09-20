# When the repository is an agent's home

Some repositories hold no software. They hold a `CLAUDE.md`, skills, plugin settings, a memory, and a work tracker, and a person opens them in Claude Code to get an agent with rules. The section table still applies; this file says what each row means when the product is an agent.

The reader is a person deciding whether to open this repository and let the agent work, or to fork its shape for an agent of their own.

The README of an agent's home is short, about 60 lines, and describes the agent as it will be next month, not as it was this week. An agent accumulates scripts, skills, pages, and quests every week; the README names the kinds of things that live in the repository and where, and leaves the directory listing and the tracker to name each one.

What changes:

- The one-liner names the agent, its domain, and its one defining rule. "A Claude Code agent that administers a homelab and asks before it changes anything."
- The description is the agent's job and the three or four rules that define how it works, written as you would explain the agent to a colleague, one sentence or two per rule with the example that makes it concrete. Not the whole of `CLAUDE.md`, and not a list of every tool. Then one paragraph on what the repository holds by kind: the rules file, the plugins it runs on, the memory, the tracker, a scripts directory, and what each kind is for.
- Why compares with a bare session and a `CLAUDE.md` of the reader's own, and says what the agent is not for.
- Status says who it serves (one person's systems, not a product), when it was last reset, and whether it is in daily use. One paragraph.
- Prerequisites are Claude Code, the plugins, and any local service they need.
- Install is the clone and the plugin installs.
- Usage is `claude` in the directory and one real exchange: the prompt a user types and the reply the agent gives.
- Adapting it replaces Caveats. It says what in the repository describes the owner rather than the agent, and what a fork replaces: memory pages about their hosts, a `.mcp.json` pointing at their network, a `CLAUDE.md` naming them. Readers of an agent home are mostly forkers; this is the section they came for.
- Other docs are `CLAUDE.md`, the tracker, and the memory index, one clause each.
- License is conditional. Many agent homes carry none; say so rather than choose one.

What stays out, beyond the general list:

- Every script, skill, and MCP server by name. Name the kinds and the directories; the listing names the items.
- What the agent has done. Completed quests change every week; the tracker owns them.
- What the agent has learned. Memory pages are the agent's, searched rather than read, and they change every session. No page counts.
- The owner's inventory: host names, hardware models, container counts, network layout. It is not a capability of the agent and it does not belong in public text.
- History and resets beyond the one line in Status.
- Portraits and mascots.
