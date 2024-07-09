
### 2. `main.py`

"""python

Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""


"""def longest_path(graph: list) -> int:
    # Your implementation goes here
    pass

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    pass
"""
def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    def dfs(v, visited, stack):
        visited[v] = True
        for neighbor, weight in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(v)

    n = len(graph)
    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    return stack[::-1]  # Reverse the stack to get the topological order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dist = [-float('inf')] * n

    # Initialize the distances of nodes with no incoming edges to 0
    incoming_edges = [0] * n
    for i in range(n):
        for neighbor, _ in graph[i]:
            incoming_edges[neighbor] += 1

    for i in range(n):
        if incoming_edges[i] == 0:
            dist[i] = 0

    for u in topo_order:
        if dist[u] != -float('inf'):
            for neighbor, weight in graph[u]:
                dist[neighbor] = max(dist[neighbor], dist[u] + weight)

    return max(dist)

