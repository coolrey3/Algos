"""Tests for sorting algorithms."""


from sort_algorithms.bubble_sort import BubbleSort
from sort_algorithms.insertion_sort import InsertionSort
from sort_algorithms.selection_sort import SelectionSort


class TestBubbleSort:
    def test_ascending(self):
        bs = BubbleSort([4, 5, 3, 1, 9, 8, 7])
        result = bs.sortAscending()
        assert result == [1, 3, 4, 5, 7, 8, 9]

    def test_descending(self):
        bs = BubbleSort([4, 5, 3, 1, 9, 8, 7])
        result = bs.sortDescending()
        assert result == [9, 8, 7, 5, 4, 3, 1]

    def test_already_sorted(self):
        bs = BubbleSort([1, 2, 3, 4, 5])
        result = bs.sortAscending()
        assert result == [1, 2, 3, 4, 5]

    def test_single_element(self):
        bs = BubbleSort([42])
        result = bs.sortAscending()
        assert result == [42]


class TestSelectionSort:
    def test_ascending(self):
        ss = SelectionSort([4, 5, 3, 1, 9, 8, 7])
        ss.sortAscending()
        assert ss.numberlist == [1, 3, 4, 5, 7, 8, 9]


class TestInsertionSort:
    def test_ascending(self):
        ins = InsertionSort([4, 5, 3, 1, 9, 8, 7])
        ins.sortAscending()
        assert ins.numberlist == [1, 3, 4, 5, 7, 8, 9]
