def test_one_plus_one_is_two():
    "Check that one and one are indeed two."
    assert 1 + 1 == 2


def test_import():
    from databroker import catalog

    assert "example" in list(catalog)
