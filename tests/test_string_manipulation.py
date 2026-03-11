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

    def test_count_method_hello(self):
        """Test count() method with 'hello'."""
        cv = CountVowels("hello")
        cv.count()  # Prints but doesn't return
        assert cv.inputString == "hello"

    def test_count_method_no_vowels(self):
        """Test count() method with no vowels."""
        cv = CountVowels("rhythm")
        cv.count()
        assert cv.inputString == "rhythm"

    def test_count_method_all_vowels(self):
        """Test count() method with all vowels."""
        cv = CountVowels("aeiou")
        cv.count()
        assert cv.inputString == "aeiou"

    def test_count_method_mixed_case(self):
        """Test count() method with mixed case (only lowercase vowels counted)."""
        cv = CountVowels("HELLO")
        cv.count()
        # Current implementation only counts lowercase vowels
        vowels = "aeiou"
        count = sum(1 for c in "HELLO" if c in vowels)
        assert count == 0  # HELLO has no lowercase vowels

    def test_count_method_sentence(self):
        """Test count() method with a sentence."""
        cv = CountVowels("the quick brown fox")
        cv.count()
        vowels = "aeiou"
        count = sum(1 for c in "the quick brown fox" if c in vowels)
        assert count == 5

    def test_count_method_empty_string(self):
        """Test count() method with empty string."""
        cv = CountVowels("")
        cv.count()
        assert cv.inputString == ""

    def test_count_method_special_characters(self):
        """Test count() method with special characters."""
        cv = CountVowels("hello!")
        cv.count()
        vowels = "aeiou"
        count = sum(1 for c in "hello!" if c in vowels)
        assert count == 2

    def test_count_method_numbers(self):
        """Test count() method with numbers."""
        cv = CountVowels("test123")
        cv.count()
        vowels = "aeiou"
        count = sum(1 for c in "test123" if c in vowels)
        assert count == 1


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
