from networkx.classes.graph import Graph
from networkx.generators.random_graphs import erdos_renyi_graph
import networkx as nx

g = erdos_renyi_graph(10,0.5)
if not isinstance(g,Graph):
    raise ValueError("Unable to generate a graph")
print(g.edges)
print(nx.to_numpy_matrix(g))

