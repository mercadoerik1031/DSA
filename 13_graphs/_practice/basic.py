from typing import List, Dict, Set
from collections import defaultdict, deque

# Num 1. Build an adjacency list
def construct_adjacency_list(edges: List[List[int]]) -> Dict[int, List[int]]:
    """
    Constructs an adjacency list representation of an undirected graph.
    """
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return dict(adjacency_list)


# Num 2. Traverse with BFS
def bfs(node: int, graph: Dict[int, List[int]]) -> Set[int]:
    """
    Performs BFS traversal of the graph starting from the given node.
    """
    visited = set()
    
    if not graph:
        return visited

    queue = deque([node])
    visited.add(node)
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


# Num 3. Traverse with DFS
def dfs(node: int, graph: Dict[int, List[int]], visited: Set[int] = None) -> Set[int]:
    """
    Performs DFS traversal of the graph starting from the given node.
    """
    if visited is None:
        visited = set()

    if not graph:
        return visited
    
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
    return visited


edges = [[0, 1], [1, 2], [2, 0]]
graph = construct_adjacency_list(edges)
print(f"Adjacency List: {graph}")

bfs_visited = bfs(0, graph)
print(f"Nodes Visited BFS: {bfs_visited}")

dfs_visited = dfs(0, graph)
print(f"Nodes Visited DFS: {dfs_visited}")
