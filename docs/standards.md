# Standards

## Principles

Adapted from [webpro/programming-principles](https://github.com/webpro/programming-principles), picked for four people working in parallel for two weeks.

**We follow:**
- **Simplest thing that works (KISS).** Choose the plainest solution that meets the step's goal.
- **YAGNI.** Build what the current step needs. No options, flags or layers "for later".
- **Separation of concerns.** Fetching data, turning it into signals and showing it are separate modules.
- **Code for the maintainer.** The next reader is a teammate who wasn't there. Clear names over clever code. Comments explain why, not what.
- **Optimise for deletion.** Small modules with narrow interfaces, so a weak piece can be replaced without touching the rest.
- **Low coupling, high cohesion.** A source adapter knows nothing about other adapters or the UI.
- **Hide what changes.** SerpApi parameters, response shapes and pagination stay inside the client and the adapters.
- **FIRST tests, written Arrange-Act-Assert.** Fast, isolated, repeatable, self-checking, and written alongside the code.

**We adapt:**
- **DRY on the third repeat.** Two similar pieces of code can stay separate. Extract a helper when a third appears, and do it in its own step if that touches other steps' code.

**We don't follow:**
- **The Boy Scout Rule.** No drive-by cleanups of code another step owns. List it under "Follow-ups" in your step record and open a new step.
- **Full SOLID.** Too much structure for a two-week project. Plain functions and small modules are fine.

## Project rules

- All SerpApi calls go through `src/ipolens/serp/client.py`. Nothing else imports `serpapi`.
- One adapter per engine in `src/ipolens/sources/`. Every result carries its source, its query parameters (without the key) and its fetch time.
- Signals from different sources are never averaged or merged into one number. Show them side by side.
- Every company gets the same fixed set of comparisons, and the brief shows each one even when nothing differs.
- A comparison sets like against like: Maps against Maps, Play Store against Play Store.
- Comparison wording is neutral: "differs from", "higher than", "lower than". Never "misleading", "false", "red flag" or other words that claim to know intent.
- Every entry in a claims file links to where the company said it. Peers follow the rule in `docs/architecture.md`.
- Every signal documents its method in a docstring and in the UI: what was counted, over what window, and what it can't tell you.
- Treat every field in a SerpApi response as optional. Missing data shows as "not available", never as zero.
- The product describes evidence. No wording that recommends buying, selling, subscribing or avoiding, and no predictions.

## Avoid

- Base classes or wrappers with a single implementation
- Config options nobody asked for
- Catching an exception only to log it and carry on. Handle it or let it surface.
- Leftover `print` debugging and commented-out code
- Unnamed numbers in scoring code. Name each constant and say where the value comes from.

## Testing

Required before a step counts as done:
- Adapters and signal code have at least one test running on a recorded response from `tests/fixtures/`.
- A bug fix comes with a test that fails without the fix.
- `uv run ruff check`, `uv run ruff format --check` and `uv run pytest` pass.

Not required: tests for Streamlit UI code. Check it by running the app.

No test calls the live SerpApi. To add a fixture, fetch through the client, scrub it (see Security) and save it under `tests/fixtures/<engine>/`.

## Formatting and linting

Ruff does both, configured in `pyproject.toml` once the project skeleton step creates it. Don't hand-format, and don't debate style Ruff already decides.

## Commits and branches

- Branch as `step/<NNN>-<short-slug>` from the latest `main`. `NNN` is the issue number padded to three digits, so issue #7 is `step/007-trends-adapter`.
- Commit subject: imperative, under 72 characters, no trailing period. The body explains why, when that isn't obvious.
- The last line of every commit is `Step: #<id>`.
- Co-author lines are only for teammates who worked on the commit. No other trailers or footers.
- To update a branch, merge `main` into it. Don't rebase commits you've pushed.
- PRs merge with a merge commit, after approval from a teammate who isn't the author. No squash or rebase merges.
- Commit these: `docs/brief.md`, the other docs, and step records. Keep these local (gitignored): `docs/research/`, `docs/handoffs/`, `cache/`, `.env`.

## Prose

Applies to text people read: README, CONTRIBUTING, docs, PR descriptions and commit messages.

- Voice: plain and direct, like a student team explaining its project to a developer. Short sentences. Say what it does, then how.
- Avoid: "revolutionary", "seamless", "leverage", "cutting-edge", "robust", "powerful", "unlock", "empower". No exclamation marks, no emoji in docs, and no claims the demo can't show.

## Security

The repository is public.

- The SerpApi key, and any LLM key, live in `.env`, which is gitignored. `.env.example` lists the variable names with empty values.
- If a key is ever committed, tell the team straight away and rotate the key in the SerpApi dashboard before anything else. Deleting it from the file doesn't remove it from history.
- Never log or print API keys, SerpApi request URLs (they include `api_key`) or full raw responses.
- Before committing a recorded response, remove `search_metadata`, reviewer names, avatars, profile links and any other personal data.
- Team members' phone numbers and emails stay out of the repo.
- Validate the company name at the UI before it reaches the client.
- Ask before adding a dependency, and name it and the reason in your step record.
- The product must not give investment advice. See the project rules above.
- GitHub secret scanning with push protection stays on.

## Tools

Python 3.12 or newer, uv, Ruff, pytest and git. The GitHub CLI (`gh`) is optional, but it lets you open issues and PRs from the terminal.
