from conftest import load_fixture
from ipolens.sources import play_store


def answer_from_fixtures(query):
    if query["engine"] == "google_play":
        return load_fixture("google_play", query["q"].lower())
    if query["engine"] == "google_play_product" and query["product_id"] == "com.oyo.consumer":
        return load_fixture("google_play_product", "oyo")
    raise AssertionError(f"unexpected query {query}")


def test_finds_the_app_in_the_highlight_block(client_with):
    client, fake = client_with(answer_from_fixtures)

    result = play_store.fetch("OYO", client)

    assert result.details["product_id"] == "com.oyo.consumer"
    assert result.details["headline_rating"] == 4.5
    assert fake.queries[1]["gl"] == "in"
    assert fake.queries[1]["sort_by"] == "2"


def test_finds_the_app_in_the_organic_results():
    app = play_store._match_app("Atomberg", load_fixture("google_play", "atomberg"))

    assert app is not None
    assert app["product_id"] == "com.atomberg.app"


def test_reviews_keep_no_personal_fields(client_with):
    client, _ = client_with(answer_from_fixtures)

    result = play_store.fetch("OYO", client)

    assert len(result.items) == 40
    assert set(result.items[0]) == {"rating", "date", "text", "likes", "developer_replied"}


def test_signals_from_the_newest_reviews(client_with):
    client, _ = client_with(answer_from_fixtures)

    signals = {s.name: s for s in play_store.signals(play_store.fetch("OYO", client))}

    assert signals["Headline rating on the listing"].value == 4.5
    assert signals["1-star share, newest 40 reviews"].value == 27.5
    assert signals["5-star share, newest 40 reviews"].value == 60.0
    assert signals["Star split, newest 40 reviews"].value == "5★ 24 · 4★ 3 · 3★ 1 · 2★ 1 · 1★ 11"
    assert signals["Developer replies, newest 40 reviews"].value == 92.5
    assert "2026-09-19" in signals["Average rating, newest 40 reviews"].method
    assert all(s.method for s in signals.values())


def test_no_matching_app_gives_an_empty_result_and_a_note(client_with):
    client, fake = client_with(lambda query: {"organic_results": []})

    result = play_store.fetch("Nosuchbrand", client)
    signals = play_store.signals(result)

    assert result.items == []
    assert "No Play Store app" in result.notes[0]
    assert len(fake.queries) == 1  # it doesn't ask for reviews of an app it didn't find
    assert all(s.value is None for s in signals if s.name != "Headline rating on the listing")
