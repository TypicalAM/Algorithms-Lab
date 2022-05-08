from graphs import AdjencencyList, Hamilton, Vertex
from utils import GraphType
solutions = 0

def hamiltonianPaths(graph: AdjencencyList, v: Vertex, visited: list, path: list, first: bool):
    global solutions
    if len(path) == graph.size:
#        print(path)
        solutions+=1
        return
    for w in v.neighbours:
        val = w.value
        if not visited[val]:
            visited[val] = True
            path.append(w)
            hamiltonianPaths(graph, w, visited, path, first)
            visited[val] = False
            path.pop()
        if solutions and first:
            return

def findHamiltonianPaths(graph: AdjencencyList, stop_at_first: bool):
    for start in graph:
        path = [start]
        visited = [False] * graph.size
        visited[start.value] = True
        hamiltonianPaths(graph, start, visited, path, stop_at_first)

for _ in range(10):
    adj = AdjencencyList(13,0.6,GraphType.HAMILTONIAN)
    print(Hamilton.is_hamiltonian(adj, True))

exit()
try:
    findHamiltonianPaths(adj,True)
except KeyboardInterrupt:
    print('Interrupted, found the following number of solutions')
print(solutions)
