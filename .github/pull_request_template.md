Closes #<!-- step / issue number -->

## What this step does

<!-- Two or three sentences. -->

## Builds on

<!-- Earlier steps this changes or improves, e.g. "Improves #9: rewrote the review parser". Or "None". -->

## How to check it

<!-- Commands to run, or what to click in the app. -->

## Checklist

- [ ] Branch is `step/<NNN>-<slug>` and my record is `docs/steps/<NNN>-<slug>.md`, with the issue number padded to 3 digits
- [ ] I didn't change any other step's record
- [ ] Every commit ends with `Step: #<id>`
- [ ] `uv run ruff check`, `uv run ruff format --check` and `uv run pytest` pass
- [ ] No keys, `.env`, personal data or unscrubbed responses in the diff
- [ ] A teammate other than me will approve and merge this
