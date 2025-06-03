def test_text_extraction():
    from nlp.preprocessing import extract_text
    assert "hello" in extract_text(b"hello world")
