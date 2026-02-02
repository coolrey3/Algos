"""Tests for Max Binary Heap implementation."""

from data_structures.Heap_practice import MaxBinaryHeap


class TestMaxBinaryHeap:
    def test_insert_single(self):
        h = MaxBinaryHeap()
        h.insert(10)
        assert h.values == [10]

    def test_insert_maintains_max_heap(self):
        h = MaxBinaryHeap()
        h.insert(10)
        h.insert(20)
        h.insert(5)
        assert h.values[0] == 20  # Max at root

    def test_insert_multiple(self):
        h = MaxBinaryHeap()
        for val in [41, 39, 33, 18, 27, 12, 55]:
            h.insert(val)
        assert h.values[0] == 55  # 55 is max

    def test_heap_property(self):
        """Every parent should be >= its children."""
        h = MaxBinaryHeap()
        for val in [41, 39, 33, 18, 27, 12, 55]:
            h.insert(val)
        for i in range(len(h.values)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(h.values):
                assert h.values[i] >= h.values[left]
            if right < len(h.values):
                assert h.values[i] >= h.values[right]

    def test_remove_returns_max(self):
        h = MaxBinaryHeap()
        for val in [41, 39, 33, 18, 27, 12, 55]:
            h.insert(val)
        assert h.remove() == 55
        assert h.remove() == 41

    def test_remove_maintains_heap(self):
        h = MaxBinaryHeap()
        for val in [41, 39, 33, 18, 27, 12, 55]:
            h.insert(val)
        h.remove()
        # After removing max, heap property still holds
        for i in range(len(h.values)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(h.values):
                assert h.values[i] >= h.values[left]
            if right < len(h.values):
                assert h.values[i] >= h.values[right]

    def test_remove_empty(self):
        h = MaxBinaryHeap()
        assert h.remove() is None

    def test_remove_all(self):
        h = MaxBinaryHeap()
        for val in [10, 20, 30]:
            h.insert(val)
        results = []
        while True:
            r = h.remove()
            if r is None:
                break
            results.append(r)
        # Should come out in descending order
        assert results == [30, 20, 10]

    def test_insert_returns_self(self):
        h = MaxBinaryHeap()
        result = h.insert(10)
        assert result is h
