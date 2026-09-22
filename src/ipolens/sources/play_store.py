"""Play Store reviews: the reference adapter.

Every adapter follows the same pattern, so copy this file when you start yours:

1. fetch() asks SerpApi through the client and returns a SourceResult with
   cleaned items and nothing personal in them.
2. signals() turns that SourceResult into Signals, each with its method written out.

What this one does: it finds the company's app in the Play Store for India,
then reads its newest reviews. The headline rating is the one Google Play
shows on the listing, averaged over every rating the app has ever had. The
newest reviews show what people are saying right now.
"""

import re
from collections import Counter
from typing import Any

from ipolens.models import Signal, SourceResult
from ipolens.serp import SerpClient

SOURCE = "play_store"
NEWEST = 199  # the most reviews SerpApi returns in one request
INDIA = {"gl": "in", "hl": "en", "store": "apps"}


def fetch(company: str, client: SerpClient, product_id: str | None = None) -> SourceResult:
    """Read the newest reviews of the company's app.

    product_id pins which app to read, for a company whose name matches other
    apps. A claims file can hold that id.
    """
    found = client.search("google_play", {"q": company, **INDIA})
    app = _match_app(company, found.data, product_id)
    if app is None:
        return SourceResult(
            source=SOURCE,
            company=company,
            queries=[found.params],
            fetched_at=found.fetched_at,
            notes=[f"No Play Store app with '{company}' in its title was found for India."],
        )

    reviews = client.search(
        "google_play_product",
        {
            "product_id": app["product_id"],
            "all_reviews": "true",
            "sort_by": "2",
            "num": NEWEST,
            **INDIA,
        },
    )
    items = [_clean_review(r) for r in reviews.data.get("reviews", [])]
    return SourceResult(
        source=SOURCE,
        company=company,
        queries=[found.params, reviews.params],
        fetched_at=min(found.fetched_at, reviews.fetched_at),
        items=items,
        details={
            "app_title": app.get("title"),
            "product_id": app["product_id"],
            "headline_rating": app.get("rating"),
            "headline_rating_count": app.get("reviews"),
            "downloads": app.get("downloads"),
        },
        notes=_notes(company, found.data, app),
    )


def _notes(company: str, data: dict[str, Any], app: dict[str, Any]) -> list[str]:
    if not app.get("title"):  # a pinned product_id that the search didn't return
        return [f"Read the pinned app {app['product_id']}, which the search didn't return."]
    notes = [f'Matched the app "{app.get("title")}" ({app["product_id"]}).']
    others = _other_matches(company, data, app)
    if others:
        notes.append("Other apps with the same name in their title: " + ", ".join(others) + ".")
    return notes


def signals(result: SourceResult) -> list[Signal]:
    def signal(key: str, name: str, value: float | str | None, unit: str, method: str) -> Signal:
        return Signal(
            source=SOURCE,
            company=result.company,
            key=f"{SOURCE}.{key}",
            name=name,
            value=value,
            unit=unit,
            method=method,
            fetched_at=result.fetched_at,
        )

    headline = result.details.get("headline_rating")
    count = result.details.get("headline_rating_count")
    ratings = [r["rating"] for r in result.items if isinstance(r.get("rating"), (int, float))]
    dates = sorted(r["date"] for r in result.items if r.get("date"))
    n = len(ratings)
    window = f"written {dates[0][:10]} to {dates[-1][:10]}" if dates else "no dates given"
    newest = f"the newest {n} reviews on Google Play in India ({window})"
    caveat = (
        "Only people who write a review are counted, and a short window can swing on one bad day."
    )

    stars = Counter(round(r) for r in ratings)
    replied = sum(1 for r in result.items if r.get("developer_replied"))

    return [
        signal(
            "headline_rating",
            "Headline rating on the listing",
            headline,
            "stars",
            "The average Google Play shows on the app's listing in India, over every rating "
            f"the app has ever had ({count if count else 'count not shown'} ratings). "
            "It moves slowly, so it says little about recent experience.",
        ),
        signal(
            "newest_average_rating",
            f"Average rating, newest {n} reviews",
            round(sum(ratings) / n, 2) if n else None,
            "stars",
            f"The mean star rating of {newest}. {caveat}",
        ),
        signal(
            "one_star_share",
            f"1-star share, newest {n} reviews",
            round(100 * stars[1] / n, 1) if n else None,
            "%",
            f"The share of {newest} that gave 1 star. {caveat}",
        ),
        signal(
            "five_star_share",
            f"5-star share, newest {n} reviews",
            round(100 * stars[5] / n, 1) if n else None,
            "%",
            f"The share of {newest} that gave 5 stars. {caveat}",
        ),
        signal(
            "star_split",
            f"Star split, newest {n} reviews",
            " · ".join(f"{s}★ {stars[s]}" for s in range(5, 0, -1)) if n else None,
            "",
            f"How many of {newest} gave each number of stars.",
        ),
        signal(
            "developer_reply_share",
            f"Developer replies, newest {n} reviews",
            round(100 * replied / n, 1) if n else None,
            "%",
            f"The share of {newest} that have a reply from the app's developer.",
        ),
    ]


def _match_app(
    company: str, data: dict[str, Any], product_id: str | None = None
) -> dict[str, Any] | None:
    """Pick the company's app out of the results.

    Google puts its best match in "app_highlight" (OYO's app lands there) and the
    rest in "organic_results" (Atomberg's does), so look in both, in that order.

    The name has to match as a whole word, so "OYO" doesn't match "Toyota
    Connect". A word match can still pick the wrong app when the name is an
    ordinary word, as "boAt" would match a game called "Boat Simulator", so
    product_id pins the right one when we know it.
    """
    candidates = [data.get("app_highlight") or {}] + [
        item for group in data.get("organic_results", []) for item in group.get("items", [])
    ]
    if product_id:
        pinned = next((a for a in candidates if a.get("product_id") == product_id), None)
        return pinned or {"product_id": product_id}
    matches = [a for a in candidates if a.get("product_id") and _is_same_name(company, a)]
    return matches[0] if matches else None


def _is_same_name(company: str, app: dict[str, Any]) -> bool:
    return (
        re.search(rf"\b{re.escape(company)}\b", str(app.get("title", "")), re.IGNORECASE)
        is not None
    )


def _other_matches(company: str, data: dict[str, Any], chosen: dict[str, Any]) -> list[str]:
    """Other apps whose title also holds the name, so a wrong pick is visible."""
    candidates = [data.get("app_highlight") or {}] + [
        item for group in data.get("organic_results", []) for item in group.get("items", [])
    ]
    return [
        f"{a.get('title')} ({a['product_id']})"
        for a in candidates
        if a.get("product_id")
        and a["product_id"] != chosen.get("product_id")
        and _is_same_name(company, a)
    ]


def _clean_review(review: dict[str, Any]) -> dict[str, Any]:
    """Keep what the signals need.

    The reviewer's name, avatar and review id are left out, and so is the review
    text: no signal reads it, and free text can name people. A later step that
    needs it can add it back.
    """
    return {
        "rating": review.get("rating"),
        "date": review.get("iso_date"),
        "likes": review.get("likes"),
        "developer_replied": bool(review.get("response")),
    }
