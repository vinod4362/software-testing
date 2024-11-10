# tests/test_character_frequency.py

from app.character_frequency import character_frequency

def test_character_frequency():
    assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert character_frequency("aabbcc") == {"a": 2, "b": 2, "c": 2}
    assert character_frequency("abcABC") == {"a": 1, "b": 1, "c": 1, "A": 1, "B": 1, "C": 1}