"""Tests for algorithm exercises (CE files)."""

from CE1 import validAnagram
from CE10 import power
from CE11 import factorial
from CE12 import prodOfArray
from CE13 import recursiveRange
from CE24 import linearSearch
from CE25 import BinarySearch


class TestValidAnagram:
    def test_matching_anagrams(self):
        assert validAnagram("anagram", "nagaram") is True

    def test_non_anagram_different_letters(self):
        assert validAnagram("rat", "car") is False

    def test_non_anagram_different_length(self):
        assert validAnagram("awesome", "awesom") is False

    def test_empty_strings(self):
        assert validAnagram("", "") is True

    def test_same_letters_different_frequency(self):
        assert validAnagram("aaz", "zza") is False

    def test_long_anagram(self):
        assert validAnagram("texttwisttime", "timetwisttext") is True

    def test_scrambled(self):
        assert validAnagram("qwerty", "qeywrt") is True


class TestPower:
    def test_power_zero_exponent(self):
        assert power(2, 0) == 1

    def test_power_of_two(self):
        assert power(2, 2) == 4

    def test_power_of_two_four(self):
        assert power(2, 4) == 16

    def test_power_base_three(self):
        assert power(3, 3) == 27

    def test_power_base_one(self):
        assert power(1, 100) == 1


class TestFactorial:
    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_two(self):
        assert factorial(2) == 2

    def test_factorial_four(self):
        assert factorial(4) == 24

    def test_factorial_seven(self):
        assert factorial(7) == 5040

    def test_factorial_zero(self):
        assert factorial(0) == 1


class TestProductOfArray:
    def test_simple(self):
        assert prodOfArray([1, 2, 3]) == 6

    def test_with_ten(self):
        assert prodOfArray([1, 2, 3, 10]) == 60

    def test_empty(self):
        assert prodOfArray([]) == 1

    def test_single_element(self):
        assert prodOfArray([5]) == 5


class TestRecursiveRange:
    def test_six(self):
        assert recursiveRange(6) == 21

    def test_ten(self):
        assert recursiveRange(10) == 55

    def test_zero(self):
        assert recursiveRange(0) == 0

    def test_one(self):
        assert recursiveRange(1) == 1


class TestLinearSearch:
    def test_found_middle(self):
        assert linearSearch([10, 15, 20, 25, 30], 15) == 1

    def test_found_in_reverse_sorted(self):
        assert linearSearch([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 4) == 5

    def test_single_element_found(self):
        assert linearSearch([0], 0) == 0

    def test_empty_array(self):
        assert linearSearch([], 5) is False

    def test_not_found(self):
        assert linearSearch([1, 2, 3], 99) is False


class TestBinarySearch:
    def test_found_last(self):
        assert BinarySearch([2, 5, 6, 9, 13, 15, 28, 30], 30) == 7

    def test_found_early(self):
        assert BinarySearch([1, 2, 3, 4, 5], 2) == 1

    def test_found_middle(self):
        assert BinarySearch([1, 2, 3, 4, 5], 3) == 2

    def test_found_end(self):
        assert BinarySearch([1, 2, 3, 4, 5], 5) == 4

    def test_not_found(self):
        assert BinarySearch([1, 2, 3, 4, 5], 6) == -1

    def test_empty_array(self):
        assert BinarySearch([], 1) == -1
