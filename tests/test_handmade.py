"""Tests for handmade data structures."""

from data_structures.handmade.raw_array import RawArray


class TestRawArray:
    def test_insert(self):
        arr = RawArray()
        arr.insert(10)
        assert arr.x == [10]

    def test_insert_multiple(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(2)
        arr.insert(3)
        assert arr.x == [1, 2, 3]

    def test_insert_at(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(3)
        arr.insertAt(2, 1)
        assert arr.x == [1, 2, 3]

    def test_remove_at(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(2)
        arr.insert(3)
        arr.removeAt(1)
        assert arr.x == [1, 3]
