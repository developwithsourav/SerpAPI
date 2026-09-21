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
- Only teammates are credited as co-authors, contributors or reviewers anywhere in the repository. A teammate who worked on a commit can be credited in a co-author line or by name in the commit body. Sourav hid the review comments on PR #3 that came from outside the team, and is turning off automatic code review in the repository settings.

## 2026-09-22

- The brief is now built from comparisons. What a company says about itself, and the headline numbers shown for it, are set against the evidence from the seven sources and against listed peers. Divyansh agreed on three conditions, and all three are in the docs.
- The first condition defines "the story": the headline numbers SerpApi returns, plus a short hand-written claims file for each demo company with a link for every claim. That file is the one input that doesn't come through SerpApi, and nothing is scraped to fill it.
- The second is that every company gets the same fixed comparisons, shown even when nothing differs, and worded as "differs from" and never "misleading". Showing only the differences would read as a search for problems, and "misleading" claims to know intent the data can't show.
- The third is that peers come from a stated rule and are compared like with like, a Maps rating against Maps ratings. The rule takes the listed peers the company names in the Basis for Offer Price section of its offer document. If there are none, we pick up to three NSE-listed companies in the same business and write down why.
- Peers roughly triple the searches per brief, from about 15 to about 45, so the cache carries more of the load.
- Divyansh takes the project skeleton, with the Play Store adapter as the reference the others copy. Sourav reviews that PR, and Divyansh reviews #4.
- boAt's data gets captured before its IPO is expected to open on 27 Sep. Every signal shows when it was fetched, so a demo run from the cache still states the date of its data.
