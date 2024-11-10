# tests/test_item_sorter.py
from app.item_sorter import sort_items

def test_sort_items():
    assert sort_items([3, 1, 2]) == [1, 2, 3]
    assert sort_items(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]
