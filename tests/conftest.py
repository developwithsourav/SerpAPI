"""Shared test helpers. Nothing here touches the network or needs a key."""

import json
from pathlib import Path
from typing import Any

import pytest

from ipolens.serp import SerpClient

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(engine: str, name: str) -> dict[str, Any]:
    """A recorded, scrubbed SerpApi answer from tests/fixtures/<engine>/<name>.json."""
    return json.loads((FIXTURES / engine / f"{name}.json").read_text(encoding="utf-8"))


class FakeSerpApi:
    """Stands in for SerpApi. Give it a function that picks the answer for a query.

    It records every query it receives, so a test can check what was asked.
    """

    def __init__(self, answer):
        self.answer = answer
        self.queries: list[dict[str, str]] = []

    def __call__(self, query: dict[str, str]) -> dict[str, Any]:
        self.queries.append(dict(query))
        return self.answer(query)


@pytest.fixture
def client_with(tmp_path):
    """Build a SerpClient that answers from a function, with its cache in a temp folder."""

    def build(answer, **kwargs) -> tuple[SerpClient, FakeSerpApi]:
        fake = FakeSerpApi(answer)
        return SerpClient(cache_dir=tmp_path / "cache", fetch=fake, **kwargs), fake

    return build
