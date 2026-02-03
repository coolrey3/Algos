class ReverseString:
    def __init__(self) -> None:
        pass

    def reverse(self, string):
        letters = []
        reversedstring = ""
        for x in string:
            letters.append(x)
        print(letters)

        for x in range(len(letters)):
            reversedstring = reversedstring + letters.pop()
        print(reversedstring)
