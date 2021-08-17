# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # print(l1)
        # print(l2)
        
        
        # while l1.next != None and l2.next != None:
        
        
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next 
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            print(tail)

        if l1:
            tail.next = l1
        elif l2:
            tail.next =l2
            
        return dummy.next

# s =Solution()
# l1 = ListNode(1,2)
# l1.next = ListNode(2,4)
# print(l1)
# s.mergeTwoLists([1,2,4],[1,3,4])

test = '1'
print(test.isalpha())
print(test.isdecimal())
test.isnumeric