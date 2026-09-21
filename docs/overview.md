# Overview

## What this is

IPO Lens builds an evidence brief for a company that is about to list on an Indian stock exchange. The prospectus tells you what the company says about itself. IPO Lens shows what everyone else is saying. It looks at app reviews, search interest across states, hiring, reviews of the company's stores and news coverage, all pulled live through SerpApi. Each signal comes with its source, how any number was worked out, and when the data was fetched.

The brief is built from comparisons, the same set for every company. Some put a number the company states, or the headline figure on one of its listings, next to what the sources show. The rating at the top of a Play Store page, for example, sits next to the ratings in the latest reviews. Others put the company next to listed peers on the same measure, Maps ratings against Maps ratings. Every comparison is shown, including the ones where nothing differs.

We're building it for the SerpApi India Hackathon 2026, in the Commerce & Market Intelligence track. None of us belong to a partner community, so we're competing for the overall places and best in track.

## Who it is for

Retail investors in India who want more than the prospectus and a few headlines before deciding whether an IPO is worth a closer look. Many of them are applying for the first time. It's also useful to students and anyone learning to research a company from public data.

## Done looks like

For the hackathon submission on 5 Oct 2026:

- One command sets it up and one command runs it locally.
- For a chosen company it pulls at least five sources, including Play Store reviews, Google Trends by state, Google Jobs, Maps reviews and news.
- Every signal shows its source, its method and when it was fetched. Sources are never blended into a single number.
- Every company gets the same comparisons, against its own stated numbers and against listed peers chosen by a stated rule, and all of them are shown whether or not anything differs.
- The brief works without an LLM key. With one, it adds a written summary that cites the signals it draws on.
- Responses are cached, so running the demo and the tests doesn't use up credits.
- A demo under three minutes shows it working for two or three real companies.

## Explicitly out of scope

- Recommendations of any kind: buy, sell, subscribe, avoid, or a score that implies one.
- Predicting listing gains, prices or the grey market premium.
- Calling a claim misleading or false. The brief says where two numbers differ and shows both.
- Fetching data from anywhere except SerpApi, including scraping sites directly. The one other input is a short hand-written claims file for each demo company, with a link for every claim.
- User accounts, saved lists, alerts, hosting and deployment.
- Markets outside India.
