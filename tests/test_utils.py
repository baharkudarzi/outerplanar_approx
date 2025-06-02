import networkx as nx
import subprocess
from pathlib import Path
from outerplanar_approx.utils import read_edgelist, write_edgelist


def test_read_write_edgelist(tmp_path):
    G = nx.Graph()
    G.add_edge('a','b')
    in_file = tmp_path / 'in.edgelist'
    out_file = tmp_path / 'out.edgelist'
    write_edgelist(nx.DiGraph(G.edges()), in_file)
    G2 = read_edgelist(in_file)
    assert G2.has_edge('a','b')


def test_cli_end_to_end(tmp_path):
    # create a simple 4-cycle
    G = nx.cycle_graph(4)
    in_file = tmp_path / 'in.edgelist'
    out_file = tmp_path / 'out.edgelist'
    nx.write_edgelist(G, in_file, data=False)
    # run CLI
    result = subprocess.run(
        ['python', '-m', 'outerplanar_approx.utils', str(in_file), str(out_file)],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    # read output; nodes are strings
    R = nx.read_edgelist(out_file)
    # ensure edges match exactly (as strings)
    actual = set(R.edges())
    expected = {(str(u), str(v)) for u, v in G.edges()}
    assert actual == expected