class ReverseString():
    def __init__(self) -> None:
        pass

    def reverse(self,string):
        # declare array
        letters = []
        # split string
        reversedstring = ''
        for x in string:
            letters.append(x)
        print(letters)
        for x in range(len(letters)):
            reversedstring = reversedstring + letters.pop()  

        print(reversedstring)

        # put in array
        # pop out of array in reverse order

        ...

rs = ReverseString()
rs.reverse('Melissa')