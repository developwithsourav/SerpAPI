# Progress

_Updated: 2026-09-22_

The issue board shows who is working on what right now. This file holds the plan and the milestones. It changes in its own step when the plan changes, not as part of feature work.

## Now

Project skeleton (Divyansh, PR due 2026-09-22). `pyproject.toml` with uv, Ruff and pytest, a committed `uv.lock`, the SerpApi client with its file cache and credit budget, and the Play Store adapter with tests as the reference every other adapter copies. No other adapter can start until this lands, and `lint-and-test` stays idle until `pyproject.toml` exists.

## Next

1. Repository settings (Sourav): turn off squash and rebase merging under Settings → General → Pull requests, turn off automatic AI code review, and mark `steps-guard` and `lint-and-test` as required checks. Both have run once now, so GitHub offers them in the picker. Finish the Ruleset list in `CONTRIBUTING.md`; "Restrict updates" and "Require linear history" stay off.
2. Capture boAt before its IPO is expected to open on 27 Sep. The cache keeps raw responses, so this needs only the client: fetch boAt's seven sources now, and the adapters parse the saved responses once they exist. `cache/` is gitignored, so the capture stays on one laptop. Agree who records the demo.
3. Write the claims files for OYO, Atomberg and boAt, with each company's listed peers copied from its filing.
4. Settle the fixed comparison set and write it into `docs/architecture.md` before the comparison code starts.
5. One source adapter per person, in parallel, each following the Play Store adapter. Each needs a scrubbed fixture in `tests/fixtures/` and a test.
6. Signals and comparisons, then the brief, then the Streamlit UI, then the optional written summary.
7. Licence: add MIT.
8. Demo dry run on OYO and Atomberg once the adapters land, to confirm all seven sources return data for both.
9. Submit a complete entry around 28 Sep. The website stamps the submission time at first submit and editing never resets it, so submitting early costs nothing.
10. Feature freeze on 2 Oct. After that: test the README setup on a clean machine, record the demo, finish the description and the SerpApi usage explanation, submit.

## Done

- Brief read and recorded in `docs/brief.md`
- Project chosen: IPO Lens, Commerce & Market Intelligence track
- Workflow and rules agreed
- Data check passed on 2026-09-20: all seven sources returned India data (see `docs/architecture.md`)
- Step #2 merged on 2026-09-21. Rules, workflow, docs and both PR checks are on `main`.
- Demo companies chosen on 2026-09-21: OYO and Atomberg, plus boAt if captured before 27 Sep
- Product framing agreed on 2026-09-22: comparisons against the company's own numbers and against listed peers (see `docs/architecture.md`)

## Blocked

Nothing is blocked.
