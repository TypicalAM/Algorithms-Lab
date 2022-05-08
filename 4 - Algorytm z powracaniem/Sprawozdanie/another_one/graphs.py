from networkx.classes.graph import Graph
from networkx.classes.reportviews import EdgeView
from networkx.generators.random_graphs import erdos_renyi_graph

class Vertex:
    slots = ('value', 'neighbours', 'degree')

    def __init__(self, value: int, neighbours: list = [], degree: int = 0) -> None:
        self.value = value
        self.neighbours = neighbours
        self.degree = degree

    def __repr__(self) -> str:
        value = self.value
        neighbours = [x.value for x in self.neighbours]
        degree = self.degree
        return f'Vertex({value=}, {neighbours=}, {degree=})'

class AdjencencyList:
    def __init__(self, size: int, density: float) -> None:
        self.size = size
        self.density = density
        self.vertices = [Vertex(i) for i in range(size)]
        self.edges = self.generate_edges()
        self.fill_graph()

    def generate_edges(self) -> EdgeView:
        graph = erdos_renyi_graph(self.size, self.density)
        if not isinstance(graph,Graph):
            raise ValueError("Couldn't create an EdgeView")
        return graph.edges

    def add_edge(self, u: int, v: int):
        u_vertex = self.vertices[u]
        v_vertex = self.vertices[v]
        u_vertex.neighbours.append(v_vertex)
        v_vertex.neighbours.append(u_vertex)
        u_vertex.degree+=1
        v_vertex.degree+=1

    def fill_graph(self) -> None:
        for v1, v2 in self.edges:
            self.add_edge(v1,v2)
