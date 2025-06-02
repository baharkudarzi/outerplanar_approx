import networkx as nx
from networkx.algorithms.cycles import cycle_basis
from networkx.utils import UnionFind
import itertools

def extract_cactus(G: nx.Graph) -> nx.DiGraph:
    """
    Phase 1: Greedy triangular-cactus extraction.
    """
    cactus = nx.DiGraph()
    used = set()
    # find all triangles
    for tri in (c for c in nx.enumerate_all_cliques(G) if len(c)==3):
        u,v,w = sorted(tri)
        edges = {frozenset((u,v)), frozenset((v,w)), frozenset((w,u))}
        if edges & used: continue
        # add directed cycle
        cactus.add_edge(u,v)
        cactus.add_edge(v,w)
        cactus.add_edge(w,u)
        used |= edges
    return cactus


def add_squares(G: nx.Graph, cactus: nx.DiGraph) -> nx.DiGraph:
    """
    Phase 2: Greedy induced 4-cycle addition.
    """
    result = nx.DiGraph()
    used = set()
    # start with cactus
    for u,v in cactus.edges():
        result.add_edge(u,v)
        used.add(frozenset((u,v)))
    # examine 4-node subsets
    for quad in itertools.combinations(G.nodes(),4):
        sub = G.subgraph(quad)
        if sub.number_of_edges()!=4 or any(sub.degree(n)!=2 for n in sub):
            continue
        # extract one cycle
        cyc = cycle_basis(sub)[0]
        # orient deterministically
        m=min(cyc); i=cyc.index(m)
        fwd = cyc[i:]+cyc[:i]
        rev = list(reversed(cyc)); j=rev.index(m)
        seq = rev[j:]+rev[:j] if tuple(rev[j:]+rev[:j])<tuple(fwd) else fwd
        ce = [(seq[k],seq[(k+1)%4]) for k in range(4)]
        und = {frozenset(e) for e in ce}
        if und & used: continue
        for a,b in ce: result.add_edge(a,b)
        used |= und
    return result


def stitch_edges(G: nx.Graph, sub: nx.DiGraph) -> nx.DiGraph:
    """
    Phase 3: Connect components via single edges.
    """
    result = sub.copy()
    uf = UnionFind()
    for u,v in result.edges(): uf.union(u,v)
    for u,v in G.edges():
        if uf[u]!=uf[v]:
            result.add_edge(u,v)
            uf.union(u,v)
    return result