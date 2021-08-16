class Hashmap():

    def __init__(self,size):
        self.KeyMap = [None]*size

    def _hash(self,key):
        total = 0
        weirdPrime = 31
        calindex = min(len(self.KeyMap),100)
        # print(calindex)
        for ch in key:
            total += ord(ch)-96
            total = (total * weirdPrime) % calindex
        # print('hash: ',total)
        return total
        # print(total)

    def set(self,key,val):
        index = self._hash(key)
        # print(index)
        if self.KeyMap[index] == None:
            self.KeyMap[index] = []
        
        self.KeyMap[index].append([key,val])
        # print(self.KeyMap)
        return index
    
    def get(self,key):
        index =self._hash(key)
        if self.KeyMap[index]:
            for x in self.KeyMap[index]:
                if key in x[0]:
                    return x[1]
                else:
                    return None
            return self.KeyMap[index]
        return None
        
code = 'green'
hm = Hashmap(4)
hm.set('dog',14)
hm.set('cat',1)
hm.set('bird',44)
hm.set('wolf',13)
hm.set(code,32)
print(hm.get('bird'))
# print('Code: ',total, ' index: ', total % 11)
# t = hash('1')
# print(t)
# print(ord('a')-96)
# print(ord('z')-96)
