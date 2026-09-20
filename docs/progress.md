# Progress

_Updated: 2026-09-21_

The issue board shows who is working on what right now. This file holds the plan and the milestones. It changes in its own step when the plan changes, not as part of feature work.

## Now

Project skeleton. `pyproject.toml` with uv, Ruff and pytest, a committed `uv.lock`, and the SerpApi client with its file cache and credit budget. Everything waits on this: no adapter can start until the client exists, and `lint-and-test` stays idle until `pyproject.toml` lands.

## Next

1. Repository settings (Sourav): turn off squash and rebase merging under Settings → General → Pull requests, turn off automatic AI code review, and mark `steps-guard` and `lint-and-test` as required checks. Both have run once now, so GitHub offers them in the picker. Finish the Ruleset list in `CONTRIBUTING.md`; "Restrict updates" and "Require linear history" stay off.
2. One source adapter per person, in parallel. Each needs a scrubbed fixture in `tests/fixtures/` and a test.
3. Signals and the brief, then the Streamlit UI, then the optional written summary.
4. Licence: add MIT. The hackathon encourages an open-source licence but does not require one.
5. Demo dry run on OYO and Atomberg once the adapters land, to confirm all seven sources return data for both.
6. Submit a complete entry around 28 Sep. The website stamps the submission time at first submit and editing never resets it, so submitting early costs nothing.
7. Feature freeze on 2 Oct. After that: test the README setup on a clean machine, record the demo, finish the description and the SerpApi usage explanation, submit.

## Done

- Brief read and recorded in `docs/brief.md`
- Project chosen: IPO Lens, Commerce & Market Intelligence track
- Workflow and rules agreed
- Data check passed on 2026-09-20: all seven sources returned India data (see `docs/architecture.md`)
- Step #2 merged on 2026-09-21. Rules, workflow, docs and both PR checks are on `main`.
- Demo companies chosen on 2026-09-21: OYO and Atomberg, with boAt as a conditional third (see `docs/changes.md`)

## Blocked

Nothing is blocked. The licence question is settled: the hackathon encourages an open-source licence without requiring one, so MIT goes in as an ordinary step.
