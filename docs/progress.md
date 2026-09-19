# Progress

_Updated: 2026-09-20_

The issue board shows who is working on what right now. This file holds the plan and the milestones. It changes in its own step when the plan changes, not as part of feature work.

## Now

Step #2: project setup. Rules, workflow, docs and the two PR checks.

## Next

1. Repository settings (Sourav): finish the Ruleset list in `CONTRIBUTING.md`. "Restrict updates" and "Require linear history" must be off.
2. Project skeleton: `pyproject.toml` with uv, Ruff and pytest, and the SerpApi client with its file cache and credit budget.
3. One source adapter per person, in parallel.
4. Pick two or three demo companies whose IPOs are actually coming up. Zepto has reportedly paused its IPO and Lenskart is already listed, so neither works as the main demo.
5. Signals and the brief, then the Streamlit UI, then the optional written summary.
6. Feature freeze on 2 Oct. After that: test the README setup on a clean machine, record the demo, fill in the form, submit.

## Done

- Brief read and recorded in `docs/brief.md`
- Project chosen: IPO Lens, Commerce & Market Intelligence track
- Workflow and rules agreed
- Data check passed on 2026-09-20: all seven sources returned India data (see `docs/architecture.md`)

## Blocked

Nothing is blocked. One open decision: a licence for the repo. The hackathon encourages an open-source one, and MIT is the usual choice.
