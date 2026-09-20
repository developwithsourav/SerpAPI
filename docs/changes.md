# Change register

Project-level decisions and the reasons behind them. Step-level detail lives in `docs/steps/`. Add new entries at the bottom and never edit old ones.

## 2026-09-20

- Entered the SerpApi India Hackathon 2026 as a team of five: Sourav, Avi, Anay, Manish and Divyansh.
- Chose IPO Lens (Commerce & Market Intelligence) over a cross-language search comparison tool and a TypeScript tools package. It splits into independent pieces, nothing similar is in SerpApi's BuiltWithSerpApi gallery, and it doesn't depend on an LLM being right. Details in `architecture.md`.
- Chose Python, uv and Streamlit. Everyone knows some Python, and it's the quickest route to a working demo.
- Adopted the step workflow: an issue, a branch, a PR and a frozen record for each piece of work, a teammate's approval before merging, and merge commits only. It keeps a clear record of who did what, and nothing gets overwritten.
- Research notes and session notes stay out of the repo.
- Checked SerpApi's India data before committing to IPO Lens. Zepto, Lenskart and boAt went through all seven sources, and every one returned usable data, so we're going ahead. The findings are in `architecture.md`.
- Considered a TypeScript tools package again and stayed with Python and Streamlit.
- Step numbers follow GitHub issue numbers. #1 was a closed test PR, so project setup is step #2.
- Branch names and step records pad the number to three digits (`step/002-project-setup`, `docs/steps/002-project-setup.md`) so they sort in order and work like ticket numbers. Numbers still come from GitHub issues, never picked by hand, so two people can't take the same one. Work gets handed out by creating and assigning issues in advance.
- Review suggestions are left as comments and never committed from the browser. If a suggestion commit lands anyway, the branch's author drops it. That's the one exception to not rewriting pushed commits.
