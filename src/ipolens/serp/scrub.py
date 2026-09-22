"""Remove personal data from a SerpApi response before it is committed.

Recorded responses become test fixtures and the demo snapshot, and both are
public. scrub() drops search_metadata, drops fields that identify people, and
masks emails and phone numbers in any text that's left.

Each engine names people in different fields: Play Store reviews keep the
reviewer's name in "title", while an App Store review's "title" is its
headline. So the adapter's owner passes the extra fields to drop. A rule names
a key, and applies to the dict under that key, or to each dict in the list
under it:

    scrub(data, drop={"reviews": {"title", "id"}, "response": {"snippet"}})

From the command line, to turn a cached answer into a fixture:

    uv run python -m ipolens.serp.scrub cache/google_play_product/abc.json \\
        tests/fixtures/google_play_product/oyo.json \\
        --drop reviews:title,id,snippet --drop response:title,snippet
"""

import argparse
import json
import re
from pathlib import Path
from typing import Any

# Fields that point at a person in every engine we use.
PERSONAL_KEYS = {"avatar", "user", "author", "profile_link", "profile_picture", "contributor_id"}

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
# An Indian mobile number. The lookbehind keeps ids inside links and paths out of it, so
# ".../id6446901002", ".../6446901002" and "?id=6446901002" all survive untouched.
PHONE = re.compile(r"(?:\+?91[\s-]?)?(?<![\w/=.-])[6-9]\d{4}[\s-]?\d{5}(?![\w])")


def scrub(data: Any, drop: dict[str, set[str]] | None = None) -> Any:
    drop = drop or {}
    if isinstance(data, dict):
        data = {k: v for k, v in data.items() if k != "search_metadata" and k not in PERSONAL_KEYS}
        cleaned = {}
        for key, value in data.items():
            if key in drop and isinstance(value, dict):
                value = {k: v for k, v in value.items() if k not in drop[key]}
            elif key in drop and isinstance(value, list):
                value = [
                    {k: v for k, v in item.items() if k not in drop[key]}
                    if isinstance(item, dict)
                    else item
                    for item in value
                ]
            cleaned[key] = scrub(value, drop)
        return cleaned
    if isinstance(data, list):
        return [scrub(item, drop) for item in data]
    if isinstance(data, str):
        # A string that is only digits is an id, not something a person wrote. Without this,
        # an App Store id such as "6446901002" would come out as "[phone]". Text that holds
        # a link still gets masked: the lookbehind above is what protects ids inside links.
        if data.strip().isdigit():
            return data
        return PHONE.sub("[phone]", EMAIL.sub("[email]", data))
    return data


def _main() -> None:
    parser = argparse.ArgumentParser(description="Scrub a saved SerpApi answer into a fixture.")
    parser.add_argument("source", type=Path, help="a file under cache/, or a raw SerpApi JSON file")
    parser.add_argument("target", type=Path, help="where to write the fixture")
    parser.add_argument(
        "--drop",
        action="append",
        default=[],
        help="key:field,field to drop under that key, e.g. reviews:title,id (repeatable)",
    )
    args = parser.parse_args()

    drop: dict[str, set[str]] = {}
    for rule in args.drop:
        list_name, _, fields = rule.partition(":")
        drop.setdefault(list_name, set()).update(f for f in fields.split(",") if f)

    raw = json.loads(args.source.read_text(encoding="utf-8"))
    data = raw.get("data", raw)  # a cache file wraps the answer in "data"
    args.target.parent.mkdir(parents=True, exist_ok=True)
    args.target.write_text(
        json.dumps(scrub(data, drop), ensure_ascii=False, indent=1) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    _main()
