# 1- Find the number of vowels in a string.
# Vowels in English are A, E, O, U and I.
# Input: “hello”Output: 2


class CountVowels:
    def __init__(self, inputString):
        print(inputString)
        self.inputString = inputString

    def count(self):
        vowels = "aeiou"
        # vowels = ['a','e','i','o','u']
        count = 0
        for x in self.inputString:
            if x in vowels:
                count += 1
        print(count)
