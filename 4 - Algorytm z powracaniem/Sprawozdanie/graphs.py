from networkx.classes.graph import Graph
from networkx.classes.reportviews import EdgeView
from networkx.generators.random_graphs import erdos_renyi_graph
import random
import itertools

from utils import GraphType

class Vertex:
    slots = ('value', 'neighbours', 'degree')

    def __init__(self, value: int, neighbours: list = None, degree: int = 0) -> None:
        if not neighbours:
            neighbours = []
        self.value = value
        self.neighbours = neighbours
        self.degree = degree

    def __repr__(self) -> str:
        value = self.value
        neighbours = [x.value for x in self.neighbours]
        degree = self.degree
        return f'Vertex({value=}, {neighbours=}, {degree=})'

class AdjencencyList:
    def __init__(self, size: int, density: float, g_type: GraphType) -> None:
        '''Instanciate a graph and fill it with edges'''
        self.size = size
        self.density = density
        self.vertices = [Vertex(i) for i in range(self.size)]
        self.edges = self.generate_edges()
        if g_type == GraphType.HAMILTONIAN:
            self.hamiltonize()
        self.fill_graph()
        if g_type == GraphType.EULERIAN:
            self.eulerize()
        self.edge_num = len(self.edges)

    def __repr__(self) -> str:
        return f"AdjencencyList(size={self.size}, density={self.density}, edges={self.edge_num})"

    def __getitem__(self, key) -> Vertex:
        if not isinstance(key, int):
            raise TypeError("Access only by singular int index")
        return self.vertices[key]

    def generate_edges(self) -> EdgeView:
        '''Generate graph edges using the erdos renyi algorithm'''
        graph_gen = erdos_renyi_graph(self.size,self.density)
        if not isinstance(graph_gen,Graph):
            raise ValueError("Unable to generate a graph")
        return graph_gen.edges

    def hamiltonize(self) -> None:
        g = list(range(self.size))
        random.shuffle(g)
        g.append(g[0])
        self.edges = list(itertools.pairwise(g)) + list(self.edges)

    def eulerize(self) -> None:
        odd_vertices = [v.value for v in self if v.degree%2==1]
        new_edges = []
        while odd_vertices:
            u=random.sample(odd_vertices,1)[0]
            v=random.sample(odd_vertices,1)[0]
            while u==v:
                v=random.sample(odd_vertices,1)[0]
            odd_vertices.remove(u)
            odd_vertices.remove(v)
            self.add_edge(u,v)
            new_edges.append((u,v))
        self.edges = list(self.edges) + new_edges
        odd_vertices = [v.value for v in self if v.degree%2==1]

    def add_edge(self, u: int, v: int) -> None:
        '''Add the edge from u to v'''
        vertex_1 = self[u]
        vertex_2 = self[v]
        vertex_1.neighbours.append(vertex_2)
        vertex_2.neighbours.append(vertex_1)
        vertex_1.degree+=1
        vertex_2.degree+=1

    def fill_graph(self) -> None:
        '''Fill a graph with edges'''
        for u, v in self.edges:
            self.add_edge(u,v)

class Euler:
    @staticmethod
    def DFS(graph: AdjencencyList, v: int, discovered: list):
        discovered[v] = True
        for vertex in graph[v].neighbours:
            u = vertex.value
            if not discovered[u]:
                Euler.DFS(graph, u, discovered)
    @staticmethod
    def count_odd_vertices(graph: AdjencencyList) -> int:
        count = 0
        for v in graph:
            if v.degree & 1:
                count += 1
        return count

    @staticmethod
    def is_connected(graph: AdjencencyList) -> bool:
            discovered = [False] * graph.size
            for i in range(graph.size):
                if graph[i].degree:
                    Euler.DFS(graph, i, discovered)
                    break
            for i in range(graph.size):
                if not discovered[i] and graph[i].degree:
                    return False
            return True
    @staticmethod
    def is_eulerian(graph: AdjencencyList) -> bool:
        is_connected = Euler.is_connected(graph)
        odd_vertices = Euler.count_odd_vertices(graph)
        if is_connected and not odd_vertices:
            return True
        return False
