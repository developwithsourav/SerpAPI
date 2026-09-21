# Step #4: Sync project docs and tighten the co-author rule

- **Owner:** Sourav
- **Builds on:** #2

## What was done

- Updated `docs/progress.md`. The project skeleton is the current work, owned by Divyansh, and Next now covers capturing boAt before 27 Sep, writing the claims files and settling the comparison set.
- Added entries for 2026-09-21 and 2026-09-22 to `docs/changes.md`, on the merge method, the rules re-read, the demo companies, the co-author rule and the new framing.
- Re-read the hackathon site, Rules, Terms and submission form against `docs/brief.md` and found nothing wrong. Added the details it was missing: the licence position, who is ineligible, the checks before an award is paid, the occupation and experience fields, how the submission time is recorded, the governing law and the liability cap. Ticked the two checklist items that are now verified.
- Framed the brief around comparisons, on the three conditions Divyansh set. `docs/overview.md`, `docs/architecture.md`, `docs/standards.md`, `AGENTS.md` and the README now describe the claims file, the fixed comparison set, the neutral wording and the peer rule. The diagram in the README and in `docs/architecture.md` shows the claims file and the comparisons.
- `AGENTS.md` and `CONTRIBUTING.md` now say that only teammates are credited as co-authors, contributors or reviewers.

## Changes to earlier steps

Step #2 wrote every file this step edits. No step record was touched.

- `CONTRIBUTING.md` said to redo a dropped suggestion "with a `Co-authored-by:` line for whoever suggested it", which would have credited someone outside the team. It now covers teammates only, who can be credited in a co-author line or in the commit body.
- `docs/overview.md` and the README said the app uses no data except SerpApi. The hand-written claims file is now the one exception, and both say so.

## Decisions

- Demo companies: OYO and Atomberg, plus boAt if its data is captured before 27 Sep. Reasons are in `docs/changes.md`.
- The brief is built from comparisons, with a hand-written claims file and a stated peer rule. Reasons are in the 2026-09-22 decisions in `docs/architecture.md`.
- Claims files are TOML because Python's standard library reads it, so they add no dependency.
- Teammates who worked on a commit can still be credited, and nobody else is. We considered banning co-author lines outright and decided against it, because pairing happens and the credit should be recorded somewhere.
- `main` stays as it is after the squash merge. Its content matches the branch exactly and the author is right, and a force-push to a protected branch would cost more than the lost commit split on one docs PR.
- `step/002-project-setup` stays on GitHub because it still holds Divyansh's three separate commits.

## Known weaknesses

- The demo companies come from public IPO pipeline reporting. Nobody has run OYO or Atomberg through the seven sources yet, as was done for Zepto, Lenskart and boAt on 2026-09-20.
- Nobody has read the Basis for Offer Price sections of the OYO, Atomberg or boAt filings yet. If a filing names no listed peers, the fallback applies and those picks need their reasons written down.
- The comparison set isn't settled. The docs say how comparisons behave but not which ones exist.
- A judge who types in a company without a claims file gets comparisons against headline numbers and peers only.
- `docs/brief.md` now holds two readings taken two days apart. Only the retrieved date at the top says how old it is.

## Follow-ups

- Repository settings: squash and rebase merging off, automatic code review off, both checks required, and a decision on auto-deleting head branches.
- Add MIT as the licence.
- Run OYO and Atomberg through all seven sources once the client exists, and record the result in `docs/architecture.md` like the 2026-09-20 check.
- Settle the fixed comparison set in its own step.
- The review comments on PR #3 from outside the team are hidden, but the review entry stays on the PR timeline. GitHub doesn't delete submitted reviews.
