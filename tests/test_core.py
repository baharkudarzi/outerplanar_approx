import networkx as nx
import pytest
from outerplanar_approx.core import extract_cactus, add_squares, stitch_edges

def test_extract_cactus_empty():
    G = nx.Graph()
    H = extract_cactus(G)
    assert isinstance(H, nx.DiGraph)
    assert H.number_of_edges() == 0


def test_extract_cactus_triangle():
    G = nx.Graph()
    G.add_edges_from([(1,2),(2,3),(3,1)])
    H = extract_cactus(G)
    assert set(H.edges()) == {(1,2),(2,3),(3,1)}


def test_add_squares_empty():
    G = nx.Graph()
    H = extract_cactus(G)
    R = add_squares(G, H)
    assert R.number_of_edges() == 0


def test_add_squares_cycle4():
    G = nx.cycle_graph(4)
    H = extract_cactus(G)
    R = add_squares(G, H)
    expected = {(0,1),(1,2),(2,3),(3,0)}
    assert set(R.edges()) == expected


def test_stitch_empty():
    G = nx.Graph()
    H = extract_cactus(G)
    R = stitch_edges(G, H)
    assert R.number_of_edges() == 0


def test_stitch_two_triangles():
    G = nx.Graph()
    G.add_edges_from([(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3)])
    H = extract_cactus(G)
    R = stitch_edges(G, H)
    # Should connect two triangles via edge (2,3)
    assert R.has_edge(2,3)
    assert R.number_of_edges() == H.number_of_edges() + 1