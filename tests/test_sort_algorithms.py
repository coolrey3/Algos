"""Tests for sorting algorithms."""

from sort_algorithms.bubble_sort import BubbleSort
from sort_algorithms.insertion_sort import InsertionSort
from sort_algorithms.merge_sort import MergeSort
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

    def test_duplicates(self):
        bs = BubbleSort([3, 1, 3, 2, 1])
        result = bs.sortAscending()
        assert result == [1, 1, 2, 3, 3]

    def test_negative_numbers(self):
        bs = BubbleSort([-3, 1, -1, 2, 0])
        result = bs.sortAscending()
        assert result == [-3, -1, 0, 1, 2]


class TestSelectionSort:
    def test_ascending(self):
        ss = SelectionSort([4, 5, 3, 1, 9, 8, 7])
        ss.sortAscending()
        assert ss.numberlist == [1, 3, 4, 5, 7, 8, 9]

    def test_already_sorted(self):
        ss = SelectionSort([1, 2, 3])
        ss.sortAscending()
        assert ss.numberlist == [1, 2, 3]

    def test_reverse_sorted(self):
        ss = SelectionSort([5, 4, 3, 2, 1])
        ss.sortAscending()
        assert ss.numberlist == [1, 2, 3, 4, 5]


class TestInsertionSort:
    def test_ascending(self):
        ins = InsertionSort([4, 5, 3, 1, 9, 8, 7])
        ins.sortAscending()
        assert ins.numberlist == [1, 3, 4, 5, 7, 8, 9]

    def test_already_sorted(self):
        ins = InsertionSort([1, 2, 3])
        ins.sortAscending()
        assert ins.numberlist == [1, 2, 3]

    def test_single_element(self):
        ins = InsertionSort([42])
        ins.sortAscending()
        assert ins.numberlist == [42]


class TestMergeSort:
    def test_merge_helper(self):
        ms = MergeSort([0, 0, 0, 0])
        result = ms.merge([1, 3], [2, 4], [0, 0, 0, 0])
        assert result == [1, 2, 3, 4]

    def test_merge_unequal_halves(self):
        ms = MergeSort([0, 0, 0, 0, 0])
        result = ms.merge([1, 5], [2, 3, 4], [0, 0, 0, 0, 0])
        assert result == [1, 2, 3, 4, 5]

    def test_merge_single_elements(self):
        ms = MergeSort([0, 0])
        result = ms.merge([1], [2], [0, 0])
        assert result == [1, 2]
