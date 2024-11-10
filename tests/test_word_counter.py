# tests/test_word_counter.py
from app.word_counter import count_words, count_occurrences

def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("This is a test sentence") == 5

def test_count_occurrences():
    assert count_occurrences("Hello world", "o") == 2
    assert count_occurrences("test", "t") == 2
