"""Tests for hand-built data structures."""


from data_structures.fib import fib, fibBUp
from data_structures.Graph_practice import Graph
from data_structures.Queue_practice import Queue
from data_structures.SLL_practice import Node, SinglyLinkedList
from data_structures.Stack_practice import Node as StackNode
from data_structures.Stack_practice import Stack

# --- Singly Linked List ---

class TestSinglyLinkedList:
    def test_push_single(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        assert ll.head.data == 1
        assert ll.tail.data == 1
        assert ll.length == 1

    def test_push_multiple(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(2))
        ll.push(Node(3))
        assert ll.head.data == 1
        assert ll.tail.data == 3
        assert ll.length == 3

    def test_pop(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(2))
        ll.push(Node(3))
        popped = ll.pop()
        assert popped.data == 3
        assert ll.length == 2
        assert ll.tail.data == 2

    def test_pop_empty(self):
        ll = SinglyLinkedList()
        assert ll.pop() is None

    def test_shift(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(2))
        shifted = ll.shift()
        assert shifted.data == 1
        assert ll.head.data == 2
        assert ll.length == 1

    def test_shift_empty(self):
        ll = SinglyLinkedList()
        assert ll.shift() is None

    def test_get(self):
        ll = SinglyLinkedList()
        ll.push(Node(10))
        ll.push(Node(20))
        ll.push(Node(30))
        assert ll.get(0).data == 10
        assert ll.get(1).data == 20
        assert ll.get(2).data == 30

    def test_get_out_of_bounds(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        assert ll.get(5) is None
        assert ll.get(-1) is None

    def test_set(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(2))
        ll.set(1, 99)
        assert ll.get(1).data == 99

    def test_insert(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(3))
        ll.insert(1, Node(2))
        assert ll.get(0).data == 1
        assert ll.get(1).data == 2
        assert ll.get(2).data == 3

    def test_reverse(self):
        ll = SinglyLinkedList()
        ll.push(Node(1))
        ll.push(Node(2))
        ll.push(Node(3))
        ll.reverse()
        assert ll.head.data == 3
        assert ll.get(1).data == 2
        assert ll.tail.data == 1


# --- Stack ---

class TestStack:
    def test_push(self):
        s = Stack()
        s.push(StackNode(10))
        assert s.size == 1
        assert s.first.data == 10

    def test_push_multiple(self):
        s = Stack()
        s.push(StackNode(1))
        s.push(StackNode(2))
        s.push(StackNode(3))
        assert s.size == 3
        assert s.first.data == 3  # LIFO

    def test_pop(self):
        s = Stack()
        s.push(StackNode(1))
        s.push(StackNode(2))
        popped = s.pop()
        assert popped.data == 2
        assert s.size == 1

    def test_pop_empty(self):
        s = Stack()
        assert s.pop() is None


# --- Queue ---

class TestQueue:
    def test_enqueue(self):
        q = Queue()
        q.enqueue("first")
        assert q.first.data == "first"
        assert q.size == 1

    def test_enqueue_multiple(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")
        assert q.first.data == "a"  # FIFO
        assert q.last.data == "c"
        assert q.size == 3

    def test_dequeue(self):
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.dequeue()
        assert q.first.data == "b"
        assert q.size == 1

    def test_dequeue_empty(self):
        q = Queue()
        assert q.dequeue() is None


# --- Graph ---

class TestGraph:
    def test_add_vertex(self):
        g = Graph()
        g.addVertex("A")
        assert "A" in g.adjacenyList

    def test_add_edge(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("B")
        g.addEdge("A", "B")
        assert "B" in g.adjacenyList["A"]
        assert "A" in g.adjacenyList["B"]

    def test_remove_edge(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("B")
        g.addEdge("A", "B")
        g.removeEdge("A", "B")
        assert "B" not in g.adjacenyList["A"]
        assert "A" not in g.adjacenyList["B"]

    def test_remove_vertex(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("B")
        g.addVertex("C")
        g.addEdge("A", "B")
        g.addEdge("A", "C")
        g.removeVertex("A")
        assert "A" not in g.adjacenyList
        assert "A" not in g.adjacenyList["B"]
        assert "A" not in g.adjacenyList["C"]

    def test_dfs_recursive(self):
        g = Graph()
        for v in ["A", "B", "C", "D"]:
            g.addVertex(v)
        g.addEdge("A", "B")
        g.addEdge("A", "C")
        g.addEdge("B", "D")
        result = g.dfsRecursive("A")
        assert set(result) == {"A", "B", "C", "D"}
        assert result[0] == "A"

    def test_dfs_iterative(self):
        g = Graph()
        for v in ["A", "B", "C", "D"]:
            g.addVertex(v)
        g.addEdge("A", "B")
        g.addEdge("A", "C")
        g.addEdge("B", "D")
        result = g.dfsIterative("A")
        assert set(result) == {"A", "B", "C", "D"}
        assert result[0] == "A"


# --- Fibonacci ---

class TestFibonacci:
    def test_fib_base_cases(self):
        assert fib(1) == 1
        assert fib(2) == 1

    def test_fib_known_values(self):
        assert fib(10) == 55
        assert fib(20) == 6765

    def test_fib_bottom_up_base(self):
        assert fibBUp(1) == 1
        assert fibBUp(2) == 1

    def test_fib_bottom_up_known(self):
        assert fibBUp(10) == 55
        assert fibBUp(50) == 12586269025
