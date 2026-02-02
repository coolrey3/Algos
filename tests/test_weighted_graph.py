"""Tests for Weighted Graph implementation."""

from data_structures.Weighted_Graph import Graph


class TestWeightedGraph:
    def test_add_vertex(self):
        g = Graph()
        g.addVertex("A")
        assert "A" in g.adjacenyList
        assert g.adjacenyList["A"] == []

    def test_add_vertex_duplicate(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("A")
        assert len(g.adjacenyList) == 1

    def test_add_edge(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("B")
        g.addEdge("A", "B", 5)
        assert len(g.adjacenyList["A"]) == 1
        assert g.adjacenyList["A"][0] == {"node": "B", "weight": 5}
        assert g.adjacenyList["B"][0] == {"node": "A", "weight": 5}

    def test_add_multiple_edges(self):
        g = Graph()
        for v in ["A", "B", "C"]:
            g.addVertex(v)
        g.addEdge("A", "B", 2)
        g.addEdge("A", "C", 1)
        assert len(g.adjacenyList["A"]) == 2
        assert len(g.adjacenyList["B"]) == 1
        assert len(g.adjacenyList["C"]) == 1

    def test_edge_weights(self):
        g = Graph()
        g.addVertex("A")
        g.addVertex("B")
        g.addEdge("A", "B", 10)
        assert g.adjacenyList["A"][0]["weight"] == 10
        assert g.adjacenyList["B"][0]["weight"] == 10

    def test_complex_graph(self):
        g = Graph()
        for v in ["A", "B", "C", "D", "E", "F"]:
            g.addVertex(v)
        g.addEdge("A", "B", 2)
        g.addEdge("A", "C", 1)
        g.addEdge("B", "D", 3)
        g.addEdge("E", "C", 2)
        g.addEdge("D", "E", 3)
        g.addEdge("D", "F", 3)
        g.addEdge("E", "F", 2)
        # Check vertex count
        assert len(g.adjacenyList) == 6
        # Check adjacency for D (connected to B, E, F)
        d_neighbors = [edge["node"] for edge in g.adjacenyList["D"]]
        assert set(d_neighbors) == {"B", "E", "F"}
