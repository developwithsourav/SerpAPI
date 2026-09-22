# Progress

_Updated: 2026-09-23_

The issue board shows who is working on what right now. This file holds the plan and the milestones. It changes in its own step when the plan changes, not as part of feature work.

## Now

The skeleton is merged, so the parts run in parallel. Each adapter copies `src/ipolens/sources/play_store.py`.

- boAt capture, before its IPO is expected to open on 27 Sep. It was Manish's, so it needs an owner now. It has to use exactly the parameters each adapter will use, because the cache finds a saved answer by its parameters, so Sourav fixes the Maps city list first. Decide before the capture whether a scrubbed `demo/` snapshot gets committed, since `cache/` stays on one laptop.
- Adapters: Maps (Sourav), Trends (Avi), News and Jobs (Anay). App Store and Finance were Manish's and need owners.
- Claims files for OYO, Atomberg and boAt, with each company's listed peers and its Play Store app id (Anay).
- The comparison set: Divyansh drafts it, and the group agrees on it before `compare/` starts.
- The app screen on sample data (Avi), until the adapters land.

## Next

1. Repository: confirm automatic code review is off, which the API can't show, and add the MIT licence.
2. `docs/architecture.md`: write in the 22 Sep data check for OYO and Atomberg, take `signals/` out of the tree, since each adapter has its own `signals()`, and store the file with LF endings.
3. Comparisons (`compare/`) once the set is agreed and the adapters it uses have landed, then the brief with peer runs, then the app screen wired to real data.
4. The written summary only if time allows. It has no owner and is the first thing to drop.
5. The demo snapshot under `demo/`, scrubbed, so the app runs offline with no key.
6. Demo dry run: the whole app on OYO and Atomberg once the adapters land.
7. Submit a complete entry as soon as the app runs end to end. The website stamps the submission time at first submit and editing never resets it, so submitting early costs nothing.
8. Feature freeze on 2 Oct. After that: test the README setup on a clean machine, record the demo, finish the description and the SerpApi usage explanation, submit.

## Done

- Brief read and recorded in `docs/brief.md`
- Project chosen: IPO Lens, Commerce & Market Intelligence track
- Workflow and rules agreed
- Data check passed on 2026-09-20: all seven sources returned India data (see `docs/architecture.md`)
- Step #2 merged on 2026-09-21. Rules, workflow, docs and both PR checks are on `main`.
- Demo companies chosen on 2026-09-21: OYO and Atomberg, plus boAt if captured before 27 Sep
- Product framing agreed on 2026-09-22: comparisons against the company's own numbers and against listed peers (see `docs/architecture.md`)
- Repository settings applied on 2026-09-22: merge commits only, and the `main` ruleset requires `steps-guard` and `lint-and-test`, dismisses stale approvals and asks for approval of the latest push.
- Data check on OYO and Atomberg on 2026-09-22: all seven sources returned data.
- Step #5 merged on 2026-09-23: the project skeleton, the SerpApi client with its cache, budget and offline mode, the scrubber, and the Play Store reference adapter, with 27 tests. `lint-and-test` now runs for real.

## Blocked

Manish's parts wait on the team agreeing who takes them: the boAt capture, App Store, Finance, the demo snapshot and the README setup test. The boAt capture can't wait past 27 Sep.
