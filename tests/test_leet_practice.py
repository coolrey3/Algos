"""Tests for LeetCode practice problems."""

from data_structures.leet_practice import ListNode, Solution


class TestMergeTwoLists:
    def _make_list(self, values):
        """Helper to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _to_list(self, head):
        """Helper to convert linked list to Python list."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_merge_basic(self):
        s = Solution()
        l1 = self._make_list([1, 2, 4])
        l2 = self._make_list([1, 3, 4])
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 1, 2, 3, 4, 4]

    def test_merge_empty_first(self):
        s = Solution()
        l1 = None
        l2 = self._make_list([1, 2, 3])
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 2, 3]

    def test_merge_empty_second(self):
        s = Solution()
        l1 = self._make_list([1, 2, 3])
        l2 = None
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 2, 3]

    def test_merge_both_empty(self):
        s = Solution()
        merged = s.mergeTwoLists(None, None)
        assert merged is None

    def test_merge_single_elements(self):
        s = Solution()
        l1 = self._make_list([1])
        l2 = self._make_list([2])
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 2]

    def test_merge_already_sorted(self):
        s = Solution()
        l1 = self._make_list([1, 2])
        l2 = self._make_list([3, 4])
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 2, 3, 4]

    def test_merge_interleaved(self):
        s = Solution()
        l1 = self._make_list([1, 3, 5])
        l2 = self._make_list([2, 4, 6])
        merged = s.mergeTwoLists(l1, l2)
        assert self._to_list(merged) == [1, 2, 3, 4, 5, 6]


class TestListNode:
    def test_node_defaults(self):
        node = ListNode()
        assert node.val == 0
        assert node.next is None

    def test_node_with_value(self):
        node = ListNode(5)
        assert node.val == 5

    def test_node_chain(self):
        n3 = ListNode(3)
        n2 = ListNode(2, n3)
        n1 = ListNode(1, n2)
        assert n1.val == 1
        assert n1.next.val == 2
        assert n1.next.next.val == 3
