def test_import():
    from databroker import catalog

    assert "example" in list(catalog)
