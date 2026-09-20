# When the repository is an agent's home

Some repositories hold no software. They hold a `CLAUDE.md`, skills, plugin settings, a memory, and a work tracker, and a person opens them in Claude Code to get an agent with rules. `neckbeard` and `agent-builder` are two. The section table still applies; this file says what each row means when the product is an agent.

The reader is a person deciding whether to open this repository and let the agent work, or to fork its shape for an agent of their own.

What changes:

- The one-liner names the agent, its domain, and its one defining rule. "A Claude Code agent that administers a homelab and asks before it changes anything."
- Capabilities are the rules the agent works by and the tools it carries: the plugins, the skills, the MCP servers, the approval gate, the default it reaches for. These hold across sessions, so they belong in the README. Write them as a person would explain the agent to a colleague, a sentence or two each with the example that makes the rule concrete, not as a checklist.
- Why compares with a bare session and a `CLAUDE.md` of the reader's own, and says what the agent is not for.
- Status says who it serves (one person's systems, not a product), when it was last reset, and whether it is in daily use.
- Prerequisites are Claude Code, the plugins, and any local service they need.
- Install is the clone and the plugin installs.
- Usage is `claude` in the directory and one real exchange: the prompt a user types and the reply the agent gives.
- Caveats say what in the repository describes the owner rather than the agent: memory pages about their hosts, a `.mcp.json` pointing at their network, a `CLAUDE.md` naming them. A fork replaces those.
- Other docs are `CLAUDE.md`, the tracker, and the memory index, one clause each.
- License is conditional. Many agent homes carry none; say so rather than choose one.

What stays out, beyond the general list:

- What the agent has done. Completed quests change every week; the tracker owns them.
- What the agent has learned. Memory pages are the agent's, searched rather than read, and they change every session.
- The owner's inventory: host names, hardware models, container counts, network layout. It is not a capability of the agent and it does not belong in public text.
- History and resets beyond the one line in Status.
- Portraits and mascots.

The README of an agent's home describes the agent as it will be next month, not as it was this week.
