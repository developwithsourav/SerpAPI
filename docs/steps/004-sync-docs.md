# Step #4: Sync project docs and tighten the co-author rule

- **Owner:** Sourav
- **Builds on:** #2

## What was done

- Updated `docs/progress.md`. The project skeleton is the current work, Next is renumbered, and the licence question is closed.
- Added a 2026-09-21 entry to `docs/changes.md` on the merge method, the rules re-read, the demo companies and the co-author rule.
- Re-read the hackathon site, Rules, Terms and submission form against `docs/brief.md` and found nothing wrong. Added the details it was missing: the licence position, who is ineligible, the checks before an award is paid, the occupation and experience fields, how the submission time is recorded, the governing law and the liability cap. Ticked the two checklist items that are now verified.
- `AGENTS.md`, `CONTRIBUTING.md` and `docs/standards.md` now say that no bot or AI tool is credited as a co-author, contributor or reviewer.

## Changes to earlier steps

Step #2 wrote every file this step edits. No step record was touched.

`CONTRIBUTING.md` said to redo a dropped suggestion "with a `Co-authored-by:` line for whoever suggested it", which would have credited a review bot. It now covers teammates only, who can be credited in a co-author line or in the commit body.

## Decisions

- Demo companies: OYO and Atomberg, plus boAt if its data is captured before 27 Sep. Reasons are in `docs/changes.md`.
- Teammates who worked on a commit can still be credited. Only bots and AI tools are barred. We considered banning co-author lines outright and decided against it, because pairing happens and the credit should be recorded somewhere.
- `main` stays as it is after the squash merge. Its content matches the branch exactly and the author is right, and a force-push to a protected branch would cost more than the lost commit split on one docs PR.
- `step/002-project-setup` stays on GitHub because it still holds Divyansh's three separate commits.

## Known weaknesses

- The demo companies come from public IPO pipeline reporting. Nobody has run OYO or Atomberg through the seven sources yet, as was done for Zepto, Lenskart and boAt on 2026-09-20.
- `docs/brief.md` now holds two readings taken two days apart. Only the retrieved date at the top says how old it is.

## Follow-ups

- Repository settings: squash and rebase merging off, automatic AI code review off, both checks required, and a decision on auto-deleting head branches.
- Add MIT as the licence.
- Run OYO and Atomberg through all seven sources once the client exists, and record the result in `docs/architecture.md` like the 2026-09-20 check.
- The review bot's comments on PR #3 are hidden, but its review entry stays on the PR timeline. GitHub doesn't delete submitted reviews.
