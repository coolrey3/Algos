from collections import deque

# Regular Queue - FIFO
print("Queue")

ll = deque()  # create linked list
ll.append("test")  # append 'test' to llist
print(ll)
ll.append("work")  # append 'work' to llist
print(ll)
ll.append("play")  # append 'play' to llist
print(ll)
ll.popleft()  # remove left most value in llist (regular queue)
print(ll)
ll.popleft()  # remove left most value in llist (regular queue)
print(ll)
ll.popleft()  # remove left most value in llist (regular queue)
print(ll)
print()
print("Stack")
# Stack - LIFO
stack = deque()  # create linked list
stack.append("test")  # append 'test' to llist
print(stack)
stack.append("work")  # append 'work' to llist
print(stack)
stack.append("play")  # append 'play' to llist
print(stack)
stack.pop()  # remove right most value in llist (stack)
print(stack)
stack.pop()  # remove right most value in llist (stack)
print(stack)
stack.pop()  # remove right most value in llist (stack)
print(stack)
