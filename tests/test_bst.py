"""Tests for Binary Search Tree implementation."""

from data_structures.BST_Practice import BinarySearchTree, Node


class TestBSTNode:
    def test_node_creation(self):
        node = Node(10)
        assert node.data == 10
        assert node.left is None
        assert node.right is None

    def test_node_repr(self):
        node = Node(42)
        assert repr(node) == "42"


class TestBinarySearchTree:
    def test_insert_root(self):
        bst = BinarySearchTree()
        bst.insert(10)
        assert bst.root is not None
        assert bst.root.data == 10

    def test_insert_left(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        assert bst.root.left.data == 5

    def test_insert_right(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(15)
        assert bst.root.right.data == 15

    def test_insert_multiple(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        assert bst.root.data == 10
        assert bst.root.left.data == 5
        assert bst.root.right.data == 15
        assert bst.root.left.left.data == 3
        assert bst.root.left.right.data == 7

    def test_insert_duplicate(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(10)
        # Duplicate should not create new node
        assert bst.root.left is None
        assert bst.root.right is None

    def test_insert_returns_self(self):
        bst = BinarySearchTree()
        result = bst.insert(10)
        assert result is bst

    def test_find_existing(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        assert bst.find(10) is True
        assert bst.find(5) is True
        assert bst.find(15) is True

    def test_find_nonexistent(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        assert bst.find(99) is False

    def test_find_empty_tree(self):
        bst = BinarySearchTree()
        assert bst.find(10) is None

    def test_breadth_first_search(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        result = bst.breadth()
        data = [node.data for node in result]
        assert data == [10, 5, 15, 3, 7]

    def test_dfs_preorder(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        result = bst.dfsPre()
        data = [node.data for node in result]
        assert data == [10, 5, 3, 7, 15]

    def test_dfs_postorder(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        result = bst.dfsPost()
        data = [node.data for node in result]
        assert data == [3, 7, 5, 15, 10]

    def test_dfs_inorder(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(3)
        bst.insert(7)
        result = bst.dfsinOrder()
        data = [node.data for node in result]
        # In-order should be sorted
        assert data == [3, 5, 7, 10, 15]

    def test_dfs_inorder_sorted(self):
        """In-order traversal of BST should always produce sorted output."""
        bst = BinarySearchTree()
        for val in [15, 5, 11, 17, 33, 30, 0, 2, 45, 25, 41, 1]:
            bst.insert(val)
        result = bst.dfsinOrder()
        data = [node.data for node in result]
        assert data == sorted(data)

    def test_single_node_traversals(self):
        bst = BinarySearchTree()
        bst.insert(42)
        assert [n.data for n in bst.dfsPre()] == [42]
        assert [n.data for n in bst.dfsPost()] == [42]
        assert [n.data for n in bst.dfsinOrder()] == [42]
        assert [n.data for n in bst.breadth()] == [42]
