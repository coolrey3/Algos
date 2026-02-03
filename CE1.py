# valid anagram problem


# input: 2 strings
# output: boolean value, if strings are anagram True
#         else return false
# problem restated: given 2 strings, check if both strings
# consist of the same letters and have the same letter counts
# edge cases: empty strings, strings not matching length
# strategy: check if stings dont match length, if not return false, else continue
#           if strings empty, return False
#           declare counter object
#           iterate over first string, , append letter counts to coutns obj
#           for key in obj, check for key in second obj
# if key not in obj, return false
# if key in obj, check that values match
# if not matching return false
# else return true
# return boolean
# variables:counter object,
# complexity: O(2+2n) = O(n)


def validAnagram(v1, v2):
    if v1 == "" and v2 == "":
        return True

    if len(v1) != len(v2):
        return False

    counts = {}

    for x in v1:
        counts[x] = v1.count(x)
    # print(counts)

    for k, v in counts.items():
        if k not in v2:
            # print('letters from string1 not in string2')
            return False
        if v != v2.count(k):
            # print('all letters in string2 but not same frequency')
            return False

    return True


print(validAnagram("", ""))
print(validAnagram("aaz", "zza"))
print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "car"))
print(validAnagram("awesome", "awesom"))
print(validAnagram("amanaplanacanalpanama", "acanalmanplanpamana"))
print(validAnagram("qwerty", "qeywrt"))
# print(validAnagram('awesome','awesom'))
print(validAnagram("texttwisttime", "timetwisttext"))
