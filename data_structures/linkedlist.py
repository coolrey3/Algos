from collections import  deque

ll = deque()
ll.append('test')

print(ll)
ll.append('work')

ll.append('play')
print(ll)
ll.popleft()
print(ll)


