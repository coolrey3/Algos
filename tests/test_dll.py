"""Tests for Doubly Linked List implementation."""

from data_structures.DLL_practice import DoublyLinkedList, Node


class TestDLLNode:
    def test_node_creation(self):
        node = Node(10)
        assert node.data == 10
        assert node.previous is None
        assert node.next is None


class TestDoublyLinkedList:
    def test_push_single(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        assert dll.head.data == 1
        assert dll.tail.data == 1
        assert dll.length == 1

    def test_push_multiple(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        dll.push(Node(3))
        assert dll.head.data == 1
        assert dll.tail.data == 3
        assert dll.length == 3

    def test_push_links(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        assert dll.head.next.data == 2
        assert dll.tail.previous.data == 1

    def test_pop(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        dll.push(Node(3))
        popped = dll.pop()
        assert popped.data == 3
        assert dll.tail.data == 2
        assert dll.length == 2

    def test_pop_single_element(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.pop()
        assert dll.head is None
        assert dll.tail is None

    def test_pop_empty(self):
        dll = DoublyLinkedList()
        result = dll.pop()
        assert result is not None  # returns self for empty list

    def test_shift(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        dll.push(Node(3))
        shifted = dll.shift()
        assert shifted.data == 1
        assert dll.head.data == 2
        assert dll.length == 2

    def test_shift_single_element(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        shifted = dll.shift()
        assert shifted.data == 1
        assert dll.head is None
        assert dll.tail is None
        assert dll.length == 0

    def test_shift_empty(self):
        dll = DoublyLinkedList()
        assert dll.shift() is None

    def test_unshift(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        dll.unshift(Node(0))
        assert dll.head.data == 0
        assert dll.head.next.data == 1
        assert dll.length == 3

    def test_unshift_empty(self):
        dll = DoublyLinkedList()
        dll.unshift(Node(1))
        assert dll.head.data == 1
        assert dll.tail.data == 1
        assert dll.length == 1

    def test_get_from_beginning(self):
        dll = DoublyLinkedList()
        dll.push(Node(10))
        dll.push(Node(20))
        dll.push(Node(30))
        dll.push(Node(40))
        assert dll.get(0).data == 10
        assert dll.get(1).data == 20

    def test_get_from_end(self):
        dll = DoublyLinkedList()
        dll.push(Node(10))
        dll.push(Node(20))
        dll.push(Node(30))
        dll.push(Node(40))
        assert dll.get(3).data == 40

    def test_get_out_of_bounds(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        assert dll.get(-1) is None
        assert dll.get(5) is None

    def test_set(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        dll.push(Node(2))
        dll.push(Node(3))
        dll.set(1, 99)
        assert dll.get(1).data == 99

    def test_set_out_of_bounds(self):
        dll = DoublyLinkedList()
        dll.push(Node(1))
        result = dll.set(5, 99)
        assert result is None

    def test_repr_empty(self):
        dll = DoublyLinkedList()
        assert "empty" in repr(dll).lower()

    def test_repr_with_data(self):
        dll = DoublyLinkedList()
        dll.push(Node(5))
        r = repr(dll)
        assert "5" in r
