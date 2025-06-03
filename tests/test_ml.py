def test_dummy_classification():
    from ml.predict import classify_document
    assert classify_document("This is a lease agreement") == "Lease"
