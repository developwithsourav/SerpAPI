# IPO Lens: rules for every agent

These rules apply to every coding agent in this repository, whatever tool or model runs it. `CLAUDE.md`, `GEMINI.md` and `.agents/rules/project.md` only point here. Where a tool's defaults disagree with this file, this file wins.

IPO Lens builds an evidence brief for upcoming Indian IPOs from live search data (SerpApi). It is an entry for the SerpApi India Hackathon 2026.

## Non-negotiable: from the hackathon rules

- Deadline: 5 Oct 2026, 23:59 IST. Needs a public repo with setup instructions and a demo under 3 minutes of the project running locally.
- SerpApi must do real work in the product. No token or cosmetic calls.
- No API keys, credentials or personal data in anything committed, pushed, logged or recorded. A leak disqualifies the team.
- No copied code without a compatible licence and attribution.
- The product describes evidence. It never tells anyone to buy, sell, subscribe to or avoid an IPO, and never claims to predict listing performance.

Full brief: `docs/brief.md`

## Before you start

1. Read `docs/progress.md` and the records in `docs/steps/` that touch your area.
2. Work only on a step whose GitHub issue is assigned to your human. The issue number is the step ID.
3. Branch from the latest `main` as `step/<NNN>-<short-slug>`, where `NNN` is the issue number padded to three digits (issue #7 is `007`). Never pick a number yourself; it comes from the issue.

## Steps

A step is one issue, one branch, one PR and one record: `docs/steps/<NNN>-<slug>.md`, copied from `docs/steps/_template.md`. Commit trailers and PR links use the plain number: `Step: #7`, `Closes #7`.

- Never edit, rename or delete an existing step record. Records are frozen once merged, and the `steps-guard` check fails any PR that touches one.
- To fix or improve earlier work, open a new step. Name the step you build on in your record and say what you changed and why.
- Stay inside your step's scope. No drive-by cleanups of code another step owns. List them under "Follow-ups" in your record.
- Don't edit `docs/progress.md` in feature steps. It changes in its own step when the plan changes.

## Commits

- The last line of every commit message is the trailer `Step: #<id>`.
- Subject: imperative, under 72 characters, no trailing period.
- A commit message is a subject, an optional body and the `Step:` trailer. Add no other trailers, footers or sign-offs unless your human asks for a co-author line naming a teammate.
- PR titles describe the change. PR bodies follow the template and add nothing after it.
- The commit author is the human you work for. Never change the git identity.

## Ask your human first

- `git push`, every time
- Adding, removing or upgrading a dependency
- Deleting files
- Changing `.github/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.agents/` or `.claude/`
- Any GitHub action other than opening a PR from your own step branch

## Never

- Approve or merge a PR. A human teammate who is not the PR's author does both. You may review and comment.
- Force-push, amend or rebase pushed commits, or delete a branch that isn't yours.
- Push to `main` directly.
- Read, print or edit `.env`. `.env.example` has the variable names.
- Log or print SerpApi request URLs. They contain `api_key`.
- Call the live SerpApi from tests.
- Commit anything from `.env`, `cache/`, `docs/research/` or `docs/handoffs/`.
- Quote, cite or mention `docs/research/` in committed files, commits or PRs.

## Code

`docs/standards.md` has the full rules. The short version:

- Do the simplest thing that works. No speculative abstractions, no options nobody asked for.
- All SerpApi calls go through `src/ipolens/serp/client.py` once it exists. Nothing else imports `serpapi`.
- One adapter per engine in `src/ipolens/sources/`. Every result keeps its source label. Never average or merge signals across sources.
- Every signal documents its method in code and in the UI.
- Tests run on recorded, scrubbed responses in `tests/fixtures/`.
- Before asking for review: `uv run ruff check`, `uv run ruff format --check`, `uv run pytest`.
- Human-facing text follows the Prose section of `docs/standards.md`.

## Session notes

If your tool writes session notes or handoffs, put them in `docs/handoffs/`, which is gitignored. Anything the team needs belongs in your step record.

## Project notes

| File | Read it when |
|---|---|
| `docs/brief.md` | checking what the hackathon requires |
| `docs/overview.md` | you need to know what the product is for |
| `docs/architecture.md` | before structural or dependency changes |
| `docs/standards.md` | before writing or reviewing code |
| `docs/progress.md` | starting a session |
| `docs/steps/` | you need to know who did what, and why |
| `docs/changes.md` | you need the reasoning behind a project-level decision |
| `CONTRIBUTING.md` | you need the full team workflow |
