# Step #2: Project setup

- **Owner:** Divyansh
- **Builds on:** none

## What was done

- Recorded the hackathon brief, judging criteria and a requirements checklist in `docs/brief.md`.
- Wrote the overview, the architecture and the coding standards (`docs/overview.md`, `docs/architecture.md`, `docs/standards.md`).
- Checked SerpApi's India data before committing to the idea. Ran Zepto, Lenskart and boAt through all seven sources on 2026-09-20. Every source returned usable data. The findings are in the Sources section of `docs/architecture.md`.
- Set up the step workflow: issue and PR templates, this record format and `CONTRIBUTING.md`. Branches and records use the issue number padded to three digits, like ticket numbers (`step/002-project-setup`).
- Added the `steps-guard` check. It fails a PR that changes an existing step record, adds no record of its own, uses the wrong branch name, or has a commit without its `Step:` trailer.
- Added the `lint-and-test` check (Ruff and pytest). It stays idle until the project skeleton step adds `pyproject.toml`.
- Wrote the daily git commands, the review buddy circle and the Rulesets settings into `CONTRIBUTING.md`.
- Added `AGENTS.md` and the files that point to it, so every tool reads the same project rules.
- Added `.gitignore` and `.env.example`, and replaced the placeholder README.
- Added rules for review suggestions to `CONTRIBUTING.md`, worded by Sourav. A commit made with GitHub's Commit suggestion button had failed `steps-guard`, so it was dropped from this branch, and the rules now say how to avoid and undo that.

## Changes to earlier steps

None. Step #1 was a test PR on the README and was closed without merging.

## Decisions

See `docs/changes.md` and the decisions in `docs/architecture.md`, all dated 2026-09-20.

- CI keeps `uv sync --locked`. An unlocked sync would resolve fresh versions in CI, so it would test a different set of dependencies than anyone's laptop.

## Known weaknesses

- `steps-guard` was tested locally against eight cases, including padded and unpadded branch names. This PR is its first run on GitHub.
- The architecture is a plan. The project skeleton step will show where it's wrong.
- The data check covered three companies. Two of them won't work as the main demo: news from late August says Zepto has paused its IPO, and Lenskart is already listed.

## Follow-ups

- Choose a licence.
- Pick two or three demo companies whose IPOs are actually coming up.
- Sourav: finish the Ruleset settings in `CONTRIBUTING.md`, and mark `steps-guard` and `lint-and-test` as required checks once they have run once.
