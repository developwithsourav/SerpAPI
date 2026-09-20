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

## 2026-09-21

- Step #2 merged. Rules, workflow, docs and both PR checks are on `main`.
- The merge went in as a squash, although the workflow calls for merge commits. `main` holds one commit whose content matches the branch exactly and whose author is still Divyansh, so nothing was lost except the split into three commits. The repository settings in `CONTRIBUTING.md` hadn't been applied yet, and GitHub still offered all three merge buttons. Sourav turns off squash and rebase merging before the next PR. We aren't rewriting `main` over a docs PR, and `step/002-project-setup` stays on GitHub because it still holds the three commits.
- Re-read the hackathon site, Rules, Terms and submission form against `docs/brief.md`. Nothing in the brief was wrong, but it was missing four things that change what we do. An open-source licence is encouraged and not required, so adding MIT is our choice. The website stamps the submission time at first submit and editing never resets it, so we submit early and keep editing. The demo has to show the project running locally, which rules out recording a hosted copy. A draft needs a community source, and none of us belongs to a partner community.
- Chose OYO and Atomberg as the demo companies, with boAt as a third if we capture its data before its IPO is expected to open on 27 Sep. On paper, OYO has data in all seven sources: an app with a large volume of reviews, thousands of hotels on Maps, steady hiring, national search interest, regular news, and listed hotel companies to compare against. Atomberg has listed competitors to compare against but looks thin on Maps and app reviews, so it tests the rule that missing data shows as "not available" and never as zero.
- Rejected Zepto (postponed in August), Lenskart (already listed), PhonePe (postponed in March), Curefoods (on hold) and RentoMojo, which was still in the pipeline when we started and listed on 11 September. RentoMojo is the reason the demo runs from the cache. A company's status can change within two weeks, and a recorded demo has to replay the same way.
- No bot or AI tool is credited as a co-author, contributor or reviewer anywhere in the repository. Teammates who worked on a commit can still be credited, in a co-author line or by name in the commit body. Sourav hid the review bot's comments on PR #3 and is turning off automatic AI code review in the repository settings.
