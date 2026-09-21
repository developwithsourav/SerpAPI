# Step #5: Project skeleton

- **Owner:** Divyansh
- **Builds on:** #2

## What was done

- Set up the Python project with uv. `pyproject.toml` asks for Python 3.12 or newer, with `serpapi` and `pydantic` to run and `ruff` and `pytest` for development, and `uv.lock` is committed. Now that `pyproject.toml` exists, `lint-and-test` runs Ruff and pytest for real.
- Added `src/ipolens/serp/client.py`, the only code that calls SerpApi. It reads the key from `SERPAPI_API_KEY` or `.env`, saves every answer under `cache/` with the time it was fetched, counts the searches it spends and can stop at a budget. Its offline mode (`IPOLENS_OFFLINE=1`) only reads saved answers.
- Added `src/ipolens/models.py` with `SourceResult` and `Signal`, the two shapes every adapter returns.
- Added `src/ipolens/serp/scrub.py`. It strips `search_metadata`, fields that name people, emails and Indian phone numbers from an answer, and has a command that turns a cached answer into a test fixture.
- Added `src/ipolens/sources/play_store.py`, the adapter the others copy. It finds the company's app for India, reads the newest 199 reviews, and gives six signals: the headline rating, the recent average, the 1-star and 5-star shares, the star split and the share of reviews the developer replied to.
- Added 19 tests on scrubbed OYO and Atomberg answers. None of them needs a key or the network.

## Changes to earlier steps

None to code. `SourceResult` differs from the shape first sketched for the team: `params` became `queries`, a list, because one adapter can make several requests, and a new `details` field holds facts about the source as a whole, such as which app matched.

## Decisions

- Errors raised by the `serpapi` package include the request URL, and the URL includes the API key. The client raises its own `SerpError` with only the HTTP status and SerpApi's own message, and raises it outside the `except` block, so the new error keeps no link to the original and no traceback can show it.
- The `serpapi` package writes `api_key` into the dict it's given. The client passes it a copy and never stores that copy.
- `.env` is read by a few lines in the client instead of `python-dotenv`, which would have been a fifth dependency.
- Fixtures keep ratings, dates and likes, and leave out review text and the text of developer replies. Both can name people.
- Each adapter has its own `signals()`, so the `signals/` folder listed in `docs/architecture.md` isn't needed. #4 is changing that file right now, so the tree gets fixed after #4 merges.

## Known weaknesses

- The phone mask only knows Indian mobile numbers, and names inside review text aren't detected. That's why fixtures leave review text out.
- The newest 199 reviews covered about one day for OYO and five weeks for Atomberg, so the window varies a lot from company to company. Every method text states the window it used.
- The adapter picks the first app whose title contains the company name. That was right for OYO and Atomberg, but a brand named after a common word could match the wrong app. The note on each result says which app matched.
- A Windows terminal can't print ★ unless `PYTHONIOENCODING=utf-8` is set, so printing the star split there fails. The app screen isn't affected.
- If anyone turns on DEBUG logging, `urllib3`, which `serpapi` uses underneath, logs full request URLs, key included. Leave logging at its default level.
- `cache/` keeps raw answers, reviewer names included. Anything built from it that gets committed, such as the demo snapshot, has to go through `scrub` first.

## Follow-ups

- Write the 2026-09-22 data check into `docs/architecture.md` once #4 merges. All seven sources returned data for OYO and Atomberg. Maps means something different for each: OYO's results are its own hotels, while Atomberg's are dealers and multi-brand shops. A News search for "OYO IPO" included an unrelated article, so the News adapter needs a relevance filter.
- Take `signals/` out of the tree in `docs/architecture.md` once #4 merges.
- Candidates for the comparison set, from a live run on 2026-09-22: Atomberg's listing shows 4.3 while its newest 199 reviews average 3.76, with 20.6% at one star, and the developer replied to 1% of them. OYO's developer replied to 92.5% of its newest 40.
