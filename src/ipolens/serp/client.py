"""The only module that talks to SerpApi.

Every request goes through SerpClient.search(). It:

- adds the API key, read from SERPAPI_API_KEY or the .env file
- saves every answer under cache/ and reuses it, so a repeated search costs nothing
- counts the searches it actually spends, and can stop at a budget
- never logs, prints or stores the key, and never lets a request URL into an error

Offline mode only reads saved answers and never touches the network. The demo
snapshot uses it, and so do tests. Turn it on with IPOLENS_OFFLINE=1, or pass
offline=True.
"""

import hashlib
import json
import os
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import serpapi

Fetch = Callable[[dict[str, str]], dict[str, Any]]


class SerpError(RuntimeError):
    """A search failed. The message never contains the key or a URL."""


class NotCached(SerpError):
    """Offline mode was asked for a search it doesn't have saved."""


class BudgetExceeded(SerpError):
    """The client has already spent the number of searches it was allowed."""


@dataclass(frozen=True)
class SerpResponse:
    engine: str
    params: dict[str, str]
    """What was asked, engine included. Never the api_key."""

    data: dict[str, Any]
    fetched_at: datetime
    from_cache: bool


class SerpClient:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        cache_dir: Path | str | None = None,
        offline: bool | None = None,
        budget: int | None = None,
        fetch: Fetch | None = None,
    ):
        """
        api_key: defaults to SERPAPI_API_KEY from the environment or .env.
        cache_dir: defaults to IPOLENS_CACHE_DIR, or "cache".
        offline: defaults to IPOLENS_OFFLINE=1.
        budget: the most searches this client may spend. None means no limit.
        fetch: replaces the real SerpApi call. Tests use it.
        """
        self._api_key = api_key
        self.cache_dir = Path(cache_dir or os.environ.get("IPOLENS_CACHE_DIR") or "cache")
        self.offline = offline if offline is not None else os.environ.get("IPOLENS_OFFLINE") == "1"
        self.budget = budget
        self.searches_spent = 0
        self._fetch = fetch or self._call_serpapi

    def search(self, engine: str, params: Mapping[str, Any]) -> SerpResponse:
        if "api_key" in params:
            raise ValueError("Don't pass api_key in params; the client adds it.")
        query = {"engine": engine, **{k: str(v) for k, v in params.items()}}
        path = self._cache_path(query)

        if path.exists():
            saved = json.loads(path.read_text(encoding="utf-8"))
            return SerpResponse(
                engine=engine,
                params=saved["params"],
                data=saved["data"],
                fetched_at=datetime.fromisoformat(saved["fetched_at"]),
                from_cache=True,
            )

        if self.offline:
            raise NotCached(f"No saved answer for {engine} with {params} in {self.cache_dir}")
        if self.budget is not None and self.searches_spent >= self.budget:
            raise BudgetExceeded(f"Already spent {self.searches_spent} of {self.budget} searches")

        # Hand SerpApi a copy: the serpapi package writes api_key into the dict it's given.
        data = self._fetch(dict(query))
        self.searches_spent += 1
        fetched_at = datetime.now(UTC)

        path.parent.mkdir(parents=True, exist_ok=True)
        record = {"params": query, "fetched_at": fetched_at.isoformat(), "data": data}
        path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
        return SerpResponse(engine, query, data, fetched_at, from_cache=False)

    def _cache_path(self, query: dict[str, str]) -> Path:
        digest = hashlib.sha256(json.dumps(query, sort_keys=True).encode()).hexdigest()[:16]
        return self.cache_dir / query["engine"] / f"{digest}.json"

    def _call_serpapi(self, query: dict[str, str]) -> dict[str, Any]:
        key = self._api_key or _read_key()
        try:
            return serpapi.Client(api_key=key, timeout=60).search(query).as_dict()
        except serpapi.HTTPError as err:
            # "from None" drops the original error, whose message includes the URL and the key.
            raise SerpError(
                f"SerpApi returned HTTP {err.status_code}: {err.error or 'no details'}"
            ) from None
        except Exception as err:
            raise SerpError(f"Could not reach SerpApi ({type(err).__name__})") from None


def _read_key() -> str:
    key = os.environ.get("SERPAPI_API_KEY") or _read_env_file(Path(".env")).get("SERPAPI_API_KEY")
    if not key:
        raise SerpError("No SerpApi key. Copy .env.example to .env and fill in SERPAPI_API_KEY.")
    return key


def _read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        name, sep, value = line.partition("=")
        if sep and not name.strip().startswith("#"):
            values[name.strip()] = value.strip().strip("\"'")
    return values
