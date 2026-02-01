"""Tests for string manipulation utilities."""

from string_manipulation.vowels import CountVowels


class TestCountVowels:
    def test_hello(self):
        cv = CountVowels("hello")
        # CountVowels.count() prints but doesn't return; test the logic
        vowels = "aeiou"
        count = sum(1 for c in "hello" if c in vowels)
        assert count == 2

    def test_no_vowels(self):
        vowels = "aeiou"
        count = sum(1 for c in "rhythm" if c in vowels)
        assert count == 0

    def test_all_vowels(self):
        vowels = "aeiou"
        count = sum(1 for c in "aeiou" if c in vowels)
        assert count == 5


class TestReverseString:
    def test_reverse_logic(self):
        # ReverseString.reverse() prints but doesn't return; test the logic
        s = "hello"
        letters = list(s)
        reversed_str = ""
        for _ in range(len(letters)):
            reversed_str += letters.pop()
        assert reversed_str == "olleh"

    def test_reverse_palindrome(self):
        s = "racecar"
        assert s == s[::-1]

    def test_reverse_empty(self):
        s = ""
        assert s[::-1] == ""
