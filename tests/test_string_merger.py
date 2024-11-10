# tests/test_string_merger.py
from app.string_merger import merge_strings
from app.word_counter import count_words

def test_merge_and_count():
    merged_string = merge_strings("abc", "123")
    assert count_words(merged_string) == 1  # "a1b2c3" should be counted as a single word
