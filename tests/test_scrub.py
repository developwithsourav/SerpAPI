from ipolens.serp.scrub import scrub


def test_drops_search_metadata_and_people_fields():
    data = {
        "search_metadata": {"id": "abc", "json_endpoint": "https://serpapi.com/searches/abc.json"},
        "place": {
            "title": "OYO Townhouse",
            "user": {"name": "A Person"},
            "avatar": "https://x/y.png",
        },
    }

    cleaned = scrub(data)

    assert cleaned == {"place": {"title": "OYO Townhouse"}}


def test_drops_named_fields_from_lists_and_nested_dicts():
    data = {
        "reviews": [
            {
                "title": "A Person",
                "id": "r1",
                "rating": 1,
                "response": {"snippet": "Hi A Person", "date": "d"},
            },
        ]
    }

    cleaned = scrub(data, drop={"reviews": {"title", "id"}, "response": {"snippet"}})

    assert cleaned == {"reviews": [{"rating": 1, "response": {"date": "d"}}]}


def test_masks_emails_and_indian_phone_numbers_in_text():
    text = "Call me on +91 98765 43210 or 9876543210, or mail a.person@example.com"

    cleaned = scrub({"snippet": text})

    assert cleaned == {"snippet": "Call me on [phone] or [phone], or mail [email]"}


def test_leaves_ordinary_numbers_alone():
    data = {"rating": 4.5, "reviews": 2000000, "product_id": "1575323645", "date": "2026-09-20"}

    assert scrub(data) == data
