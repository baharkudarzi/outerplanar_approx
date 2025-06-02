import networkx as nx
import argparse
from pathlib import Path
from .core import extract_cactus, add_squares, stitch_edges

def read_edgelist(path: Path) -> nx.Graph:
    return nx.read_edgelist(path)

def write_edgelist(G: nx.DiGraph, path: Path):
    nx.write_edgelist(G, path, data=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compute a 7/10-approx outerplanar subgraph via STS")
    parser.add_argument("input", type=Path, help="Path to input edge-list file")
    parser.add_argument("output", type=Path, help="Path to write resulting subgraph")
    args = parser.parse_args()

    G = read_edgelist(args.input)
    C = extract_cactus(G)
    S = add_squares(G, C)
    R = stitch_edges(G, S)
    write_edgelist(R, args.output)