class LinearSearch():
    def __init__(self,array,search):
        self.array = array
        self.searchString = search
        print(array)

    def search(self):
        if self.searchString in self.array:
            return True
        else:
            return False

ls = LinearSearch(['q','e','g',],'y')
print(ls.search())