"""Tests for ce14.py - Fibonacci implementation"""

from ce14 import fib


class TestFibonacci:
    """Test fibonacci function from ce14.PY"""

    def test_fib_base_case_1(self):
        """Test fib(1) = 1"""
        assert fib(1) == 1

    def test_fib_base_case_2(self):
        """Test fib(2) = 1"""
        assert fib(2) == 1

    def test_fib_small_values(self):
        """Test fibonacci for small values"""
        assert fib(3) == 2
        assert fib(4) == 3
        assert fib(5) == 5
        assert fib(6) == 8
        assert fib(7) == 13

    def test_fib_medium_values(self):
        """Test fibonacci for medium values"""
        assert fib(10) == 55
        assert fib(15) == 610
        assert fib(20) == 6765

    def test_fib_sequence(self):
        """Test that fibonacci sequence is correct"""
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, val in enumerate(expected, start=1):
            assert fib(i) == val
