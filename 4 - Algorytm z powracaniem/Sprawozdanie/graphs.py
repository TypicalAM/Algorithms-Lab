from dataclasses import dataclass

from networkx.classes.graph import Graph
from networkx.classes.reportviews import EdgeView
from networkx.generators.random_graphs import erdos_renyi_graph

from utils import timing

@dataclass(slots=True)
class Vertex:
    value: int
    children: list

class AdjencencyList:
    def __init__(self, size: int, density: float) -> None:
        '''Instanciate a graph and fill it with edges'''
        self.size = size
        self.density = density
        self.graph, self.edge_num = self.generate_graph()

    def __repr__(self) -> str:
        return f"AdjencencyList(size={self.size}, density={self.density}, edges={self.edge_num})"

    def generate_edges(self) -> EdgeView:
        '''Generate graph edges using the erdos renyi algorithm'''
        graph_gen = erdos_renyi_graph(self.size,self.density)
        if not isinstance(graph_gen,Graph):
            raise ValueError("Unable to generate a graph")
        return graph_gen.edges

    def generate_graph(self) -> tuple[list[Vertex], int]:
        '''Initialize an empty graph and fill it with edges from generate_edges'''
        g = [Vertex(i,[]) for i in range(self.size)]

        edges = self.generate_edges()
        for v1, v2 in edges:
            vertex_from = g[v1]
            vertex_to = g[v2]
            vertex_from.children.append(vertex_to)
        return g, len(edges)

    @timing
    def find_eulerian_cycle(self) -> tuple[Vertex,Vertex]:
        '''Find the first eulerian cycle in the graph'''
        ...

    @timing
    def find_first_hamiltonian_cycle(self) -> tuple[Vertex,Vertex]:
        '''Find the first hamiltonian cycle in the graph'''
        ...

    @timing
    def find_all_hamiltonian_cycles(self) -> int:
        '''Find all the hamiltonian cycles in the graph'''
        ...

