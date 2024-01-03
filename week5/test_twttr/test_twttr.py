from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TwIttEr") == "Twttr"
    assert shorten("9witter") == "9wttr"
    assert shorten("twitt.r") == "twtt.r"

