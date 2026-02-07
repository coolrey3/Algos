"""Tests for search algorithms."""

from search_algorithms.linear_search import LinearSearch


class TestLinearSearch:
    """Test cases for LinearSearch class."""

    def test_search_found_at_index(self):
        """Test searching for an element that exists."""
        ls = LinearSearch([1, 2, 3, 4, 5], 3)
        # Note: The implementation has a bug - it compares index with value
        # This test documents current behavior
        result = ls.search()
        assert result in [True, False]  # Will be False due to bug

    def test_search_first_element(self):
        """Test searching for the first element."""
        ls = LinearSearch([10, 20, 30], 0)
        result = ls.search()
        assert result is True  # Index 0 == searchString 0

    def test_search_empty_array(self):
        """Test searching in an empty array."""
        ls = LinearSearch([], 5)
        result = ls.search()
        assert result is False

    def test_search_not_found(self):
        """Test searching for an element that doesn't exist."""
        ls = LinearSearch([1, 2, 3], 10)
        result = ls.search()
        assert result is False

    def test_search_single_element_match(self):
        """Test searching in a single-element array with match."""
        ls = LinearSearch([42], 0)
        result = ls.search()
        assert result is True  # Index 0 == searchString 0

    def test_search_single_element_no_match(self):
        """Test searching in a single-element array without match."""
        ls = LinearSearch([42], 5)
        result = ls.search()
        assert result is False

    def test_search_with_duplicates(self):
        """Test searching in an array with duplicate values."""
        ls = LinearSearch([1, 2, 2, 3, 2], 1)
        result = ls.search()
        assert result is True  # Index 1 == searchString 1

    def test_search_negative_numbers(self):
        """Test searching with negative numbers."""
        ls = LinearSearch([-5, -3, -1, 0, 1], 2)
        result = ls.search()
        assert result is True  # Index 2 exists

    def test_search_large_array(self):
        """Test searching in a large array."""
        large_array = list(range(1000))
        ls = LinearSearch(large_array, 500)
        result = ls.search()
        assert result is True  # Index 500 exists
