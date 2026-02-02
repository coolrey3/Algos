"""Tests for Priority Queue implementation."""

from data_structures.PrioQ_Practice import Node, PriorityQueue


class TestPriorityQueueNode:
    def test_node_creation(self):
        node = Node("task", 3)
        assert node.data == "task"
        assert node.priority == 3


class TestPriorityQueue:
    def test_enqueue_single(self):
        pq = PriorityQueue()
        pq.enqueue("task", 3)
        assert len(pq.values) == 1
        assert pq.values[0].data == "task"

    def test_enqueue_priority_order(self):
        """Lower priority number = higher urgency (min-heap)."""
        pq = PriorityQueue()
        pq.enqueue("low", 5)
        pq.enqueue("high", 1)
        pq.enqueue("mid", 3)
        # Root should have lowest priority number (highest urgency)
        assert pq.values[0].priority == 1

    def test_dequeue_returns_highest_priority(self):
        pq = PriorityQueue()
        pq.enqueue("common cold", 5)
        pq.enqueue("gun shot wound", 1)
        pq.enqueue("high fever", 4)
        pq.enqueue("broken arm", 2)
        data, priority = pq.dequeue()
        assert data == "gun shot wound"
        assert priority == 1

    def test_dequeue_order(self):
        pq = PriorityQueue()
        pq.enqueue("e", 5)
        pq.enqueue("a", 1)
        pq.enqueue("d", 4)
        pq.enqueue("b", 2)
        pq.enqueue("c", 3)

        results = []
        for _ in range(5):
            data, prio = pq.dequeue()
            results.append((data, prio))

        priorities = [r[1] for r in results]
        assert priorities == [1, 2, 3, 4, 5]

    def test_dequeue_empty(self):
        pq = PriorityQueue()
        assert pq.dequeue() is None

    def test_enqueue_returns_self(self):
        pq = PriorityQueue()
        result = pq.enqueue("x", 1)
        assert result is pq

    def test_min_heap_property(self):
        """Every parent should have priority <= its children."""
        pq = PriorityQueue()
        pq.enqueue("a", 5)
        pq.enqueue("b", 1)
        pq.enqueue("c", 4)
        pq.enqueue("d", 2)
        pq.enqueue("e", 3)
        for i in range(len(pq.values)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(pq.values):
                assert pq.values[i].priority <= pq.values[left].priority
            if right < len(pq.values):
                assert pq.values[i].priority <= pq.values[right].priority
