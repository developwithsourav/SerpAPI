import pytest
import requests
import serpapi

from ipolens.serp import BudgetExceeded, NotCached, SerpClient, SerpError


def answer_ok(query):
    return {"echo": query["q"]}


def test_first_search_is_fetched_and_saved(client_with):
    client, fake = client_with(answer_ok)

    response = client.search("google", {"q": "OYO"})

    assert response.data == {"echo": "OYO"}
    assert response.from_cache is False
    assert client.searches_spent == 1
    assert fake.queries == [{"engine": "google", "q": "OYO"}]


def test_repeat_search_comes_from_cache_and_costs_nothing(client_with):
    client, fake = client_with(answer_ok)
    first = client.search("google", {"q": "OYO"})

    second = client.search("google", {"q": "OYO"})

    assert second.from_cache is True
    assert second.data == first.data
    assert second.fetched_at == first.fetched_at
    assert client.searches_spent == 1
    assert len(fake.queries) == 1


def test_key_never_reaches_saved_params_or_cache(client_with, tmp_path):
    def answer_like_serpapi(query):
        query["api_key"] = "SECRET-KEY"  # the serpapi package does this to the dict it's given
        return {"ok": True}

    client, _ = client_with(answer_like_serpapi)

    response = client.search("google", {"q": "OYO"})

    assert "api_key" not in response.params
    saved = "".join(p.read_text(encoding="utf-8") for p in (tmp_path / "cache").rglob("*.json"))
    assert "SECRET-KEY" not in saved


def test_api_key_in_params_is_refused(client_with):
    client, _ = client_with(answer_ok)

    with pytest.raises(ValueError):
        client.search("google", {"q": "OYO", "api_key": "SECRET-KEY"})


def test_offline_reads_saved_answers(client_with, tmp_path):
    online, _ = client_with(answer_ok)
    online.search("google", {"q": "OYO"})
    offline = SerpClient(cache_dir=tmp_path / "cache", offline=True)

    response = offline.search("google", {"q": "OYO"})

    assert response.from_cache is True
    assert response.data == {"echo": "OYO"}


def test_offline_never_calls_serpapi(client_with):
    client, fake = client_with(answer_ok, offline=True)

    with pytest.raises(NotCached):
        client.search("google", {"q": "OYO"})
    assert fake.queries == []


def test_budget_stops_further_searches(client_with):
    client, fake = client_with(answer_ok, budget=1)
    client.search("google", {"q": "OYO"})

    with pytest.raises(BudgetExceeded):
        client.search("google", {"q": "Atomberg"})
    assert len(fake.queries) == 1


def test_http_error_hides_url_and_key(monkeypatch, tmp_path):
    def fail(self, params=None, **kwargs):
        response = requests.Response()
        response.status_code = 401
        response._content = b'{"error": "Invalid API key."}'
        url_error = requests.HTTPError(
            "401 Client Error: Unauthorized for url: https://serpapi.com/search?api_key=SECRET-KEY",
            response=response,
        )
        raise serpapi.HTTPError(url_error)

    monkeypatch.setattr(serpapi.Client, "search", fail)
    client = SerpClient(api_key="SECRET-KEY", cache_dir=tmp_path)

    with pytest.raises(SerpError) as caught:
        client.search("google", {"q": "OYO"})

    assert "SECRET-KEY" not in str(caught.value)
    assert "http" not in str(caught.value).lower().replace("http 401", "")
    assert "Invalid API key." in str(caught.value)
    assert caught.value.__context__ is None and caught.value.__cause__ is None


def test_connection_error_hides_url_and_key(monkeypatch, tmp_path):
    def fail(self, params=None, **kwargs):
        raise ConnectionError("Max retries exceeded with url: /search?api_key=SECRET-KEY")

    monkeypatch.setattr(serpapi.Client, "search", fail)
    client = SerpClient(api_key="SECRET-KEY", cache_dir=tmp_path)

    with pytest.raises(SerpError) as caught:
        client.search("google", {"q": "OYO"})

    assert "SECRET-KEY" not in str(caught.value)
    assert caught.value.__context__ is None and caught.value.__cause__ is None


def test_missing_key_explains_what_to_do(monkeypatch, tmp_path):
    monkeypatch.delenv("SERPAPI_API_KEY", raising=False)
    monkeypatch.chdir(tmp_path)  # no .env here
    client = SerpClient(cache_dir=tmp_path / "cache")

    with pytest.raises(SerpError, match=".env.example"):
        client.search("google", {"q": "OYO"})
