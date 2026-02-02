"""Tests for HashMap implementation."""

from data_structures.HashMap_practice import Hashmap


class TestHashmap:
    def test_set_and_get(self):
        hm = Hashmap(10)
        hm.set("dog", 14)
        assert hm.get("dog") == 14

    def test_get_nonexistent(self):
        hm = Hashmap(10)
        assert hm.get("missing") is None

    def test_set_multiple(self):
        hm = Hashmap(10)
        hm.set("dog", 14)
        hm.set("cat", 1)
        hm.set("bird", 44)
        assert hm.get("dog") == 14
        assert hm.get("cat") == 1
        assert hm.get("bird") == 44

    def test_keys(self):
        hm = Hashmap(10)
        hm.set("dog", 14)
        hm.set("cat", 1)
        hm.set("bird", 44)
        keys = hm.keys()
        assert set(keys) == {"dog", "cat", "bird"}

    def test_values(self):
        hm = Hashmap(10)
        hm.set("dog", 14)
        hm.set("cat", 1)
        hm.set("bird", 44)
        values = hm.values()
        assert values == {14, 1, 44}

    def test_items(self):
        hm = Hashmap(10)
        hm.set("a", 1)
        hm.set("b", 2)
        items = hm.items()
        # items returns list of [key, value] pairs
        item_dict = {item[0]: item[1] for item in items}
        assert item_dict["a"] == 1
        assert item_dict["b"] == 2

    def test_hash_deterministic(self):
        hm = Hashmap(10)
        h1 = hm._hash("test")
        h2 = hm._hash("test")
        assert h1 == h2

    def test_hash_within_bounds(self):
        hm = Hashmap(10)
        for key in ["a", "b", "hello", "world", "python"]:
            h = hm._hash(key)
            assert 0 <= h < len(hm.KeyMap)

    def test_collision_handling(self):
        # Small size forces collisions
        hm = Hashmap(2)
        hm.set("a", 1)
        hm.set("b", 2)
        hm.set("c", 3)
        keys = hm.keys()
        assert len(keys) == 3

    def test_values_deduplication(self):
        hm = Hashmap(10)
        hm.set("a", 1)
        hm.set("b", 1)
        hm.set("c", 1)
        # values() returns a set, so duplicates removed
        assert hm.values() == {1}

    def test_empty_hashmap(self):
        hm = Hashmap(5)
        assert hm.keys() == []
        assert hm.values() == set()
        assert hm.items() == []
