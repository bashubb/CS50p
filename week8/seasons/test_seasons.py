from seasons import convert_to_words
from datetime import date

def test_convert_words():
    assert convert_to_words(date.fromisoformat("1999-01-01")) == "Thirteen million, one hundred twenty-eight thousand, four hundred eighty minutes"
    assert convert_to_words(date.fromisoformat("2022-04-02")) == "Nine hundred thousand minutes"



