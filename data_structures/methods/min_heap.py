from binarytree import heap

# Min heap of given height
root = heap(height = 3, is_max = False)
print('Min Heap of given height', root)

root2 = heap(height = 4,is_max=False,is_perfect=True)
print('Perfect Min heap of given height', root2)