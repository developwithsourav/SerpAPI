"""The shapes every part of IPO Lens passes around.

An adapter turns SerpApi responses into a SourceResult, then into Signals.
Everything after the adapters (comparisons, the brief, the app screen) only
reads these two shapes, so each part can be built and tested on its own.

Change these carefully: every adapter depends on them. Add fields with
defaults; don't rename or remove one without telling the whole team.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class SourceResult(BaseModel):
    """What one adapter found for one company."""

    source: str
    """Short name of the source, e.g. "play_store" or "maps"."""

    company: str
    """The name that was searched, as the user typed it."""

    queries: list[dict[str, str]]
    """The parameters of every SerpApi request made, engine included. Never the api_key."""

    fetched_at: datetime
    """When SerpApi answered. With several requests, the oldest answer."""

    items: list[dict[str, Any]] = Field(default_factory=list)
    """Cleaned records, such as one per review. No personal data."""

    details: dict[str, Any] = Field(default_factory=dict)
    """Facts about the source as a whole, such as which app matched."""

    notes: list[str] = Field(default_factory=list)
    """Things a reader should know, e.g. "no app matched the name"."""


class Signal(BaseModel):
    """One number or fact taken from a SourceResult, with how it was worked out."""

    source: str
    company: str

    key: str
    """A stable id, e.g. "play_store.one_star_share".

    Comparisons find signals by key, so it never changes and never mentions a
    count, a date or anything else that shifts between companies.
    """

    name: str
    """What the screen shows, e.g. "1-star share, newest 199 reviews"."""

    value: float | str | None
    """None means the data wasn't available. Never use 0 for that."""

    unit: str = ""
    method: str
    """What was counted, over what window, and what it can't tell you."""

    fetched_at: datetime
