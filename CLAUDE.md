@AGENTS.md

# Claude Code

`AGENTS.md` above holds the project rules. This file only adds what is specific to Claude Code.

- `.claude/settings.json` turns off commit and PR attribution, asks before every `git push`, and blocks PR merges, PR reviews, force-pushes and access to `.env`. Don't work around it.
- Human-facing text (README, CONTRIBUTING, docs, PR descriptions, commit messages) goes through the `humanizer` skill before it lands.
- Commit and push with the `ship` skill, following the commit rules in `AGENTS.md`.
- Run `/security-review` before opening a PR that touches the SerpApi client, fixtures or anything that handles keys.
- At session start, read `docs/progress.md` and the newest file in `docs/handoffs/` if there is one.
- Handoffs go in `docs/handoffs/`, named `YYYY-MM-DD-HHMM-topic.md`. Never overwrite one.
