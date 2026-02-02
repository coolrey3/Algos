"""Tests for handmade data structures."""

from data_structures.handmade.raw_array import RawArray
from data_structures.handmade.raw_binary_tree import BinaryTree
from data_structures.handmade.raw_binary_tree import Node as BTNode
from data_structures.handmade.raw_linked_list import LinkedList
from data_structures.handmade.raw_linked_list import Node as LLNode
from data_structures.handmade.raw_trie import Node as TrieNode
from data_structures.handmade.raw_trie import Trie


class TestRawArray:
    def test_insert(self):
        arr = RawArray()
        arr.insert(10)
        assert arr.x == [10]

    def test_insert_multiple(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(2)
        arr.insert(3)
        assert arr.x == [1, 2, 3]

    def test_insert_at(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(3)
        arr.insertAt(2, 1)
        assert arr.x == [1, 2, 3]

    def test_remove_at(self):
        arr = RawArray()
        arr.insert(1)
        arr.insert(2)
        arr.insert(3)
        arr.removeAt(1)
        assert arr.x == [1, 3]

    def test_insert_returns_list(self):
        arr = RawArray()
        result = arr.insert(5)
        assert result == [5]

    def test_insert_at_beginning(self):
        arr = RawArray()
        arr.insert(2)
        arr.insert(3)
        arr.insertAt(1, 0)
        assert arr.x == [1, 2, 3]

    def test_empty_array(self):
        arr = RawArray()
        assert arr.x == []


class TestRawLinkedList:
    def test_node_creation(self):
        node = LLNode("a")
        assert node.data == "a"
        assert node.next is None

    def test_node_repr(self):
        node = LLNode("hello")
        assert repr(node) == "hello"

    def test_linked_list_empty(self):
        ll = LinkedList()
        assert ll.head is None

    def test_linked_list_chain(self):
        ll = LinkedList()
        n1 = LLNode("a")
        n2 = LLNode("b")
        n3 = LLNode("c")
        ll.head = n1
        n1.next = n2
        n2.next = n3
        # Traverse
        assert ll.head.data == "a"
        assert ll.head.next.data == "b"
        assert ll.head.next.next.data == "c"
        assert ll.head.next.next.next is None

    def test_linked_list_repr(self):
        ll = LinkedList()
        n1 = LLNode("a")
        n2 = LLNode("b")
        ll.head = n1
        n1.next = n2
        r = repr(ll)
        assert "a" in r
        assert "b" in r
        assert "None" in r


class TestRawBinaryTree:
    def test_node_creation(self):
        node = BTNode("10")
        assert node.data == "10"
        assert node.lchild is None
        assert node.rchild is None

    def test_tree_root(self):
        bt = BinaryTree()
        assert bt.root is None
        node = BTNode("5")
        bt.root = node
        assert bt.root.data == "5"

    def test_tree_children(self):
        bt = BinaryTree()
        root = BTNode("10")
        left = BTNode("5")
        right = BTNode("15")
        bt.root = root
        root.lchild = left
        root.rchild = right
        assert bt.root.lchild.data == "5"
        assert bt.root.rchild.data == "15"


class TestRawTrie:
    def test_trie_node(self):
        node = TrieNode("c")
        assert node.data == "c"
        assert node.child is None
        assert node.word is False

    def test_trie_chain(self):
        n1 = TrieNode("c")
        n2 = TrieNode("a")
        n3 = TrieNode("t")
        n1.child = n2
        n2.child = n3
        n3.word = True
        assert n1.child.child.data == "t"
        assert n3.word is True

    def test_trie_creation(self):
        trie = Trie()
        assert trie.root is None
        assert trie.children == []

    def test_trie_with_word(self):
        n1 = TrieNode("h")
        n2 = TrieNode("i")
        n1.child = n2
        n2.word = True
        trie = Trie()
        trie.root = n1
        trie.children.append("h")
        assert trie.root.data == "h"
        assert trie.root.child.word is True
