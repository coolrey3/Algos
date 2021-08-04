
#* Time Complexity Best: O(1) | Worst: O(n)

class LinearSearch():
    def __init__(self,array,search):
        self.array = array
        self.searchString = search
        print(array)

    def search(self):
        for x in self.array:
            if x == self.searchString:
                return True
        else:
            return False
