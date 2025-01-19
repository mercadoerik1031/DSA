from basic import construct_adjacency_list, bfs, dfs


def test_construct_adjacency_list():
    edges = [[0, 1], [1, 2], [2, 0]]
    expected = {0: [1, 2], 1: [0, 2], 2: [1, 0]}
    assert construct_adjacency_list(edges) == expected

    edges = [[0, 1], [2, 3], [4, 5]]
    expected = {0: [1], 1: [0], 2: [3], 3: [2], 4: [5], 5: [4]}
    assert construct_adjacency_list(edges) == expected

    edges = []
    expected = {}
    assert construct_adjacency_list(edges) == expected


def test_bfs():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert bfs(0, graph) == {0, 1, 2}
    assert bfs(1, graph) == {0, 1, 2}

    graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    assert bfs(0, graph) == {0, 1, 2, 3}
    assert bfs(3, graph) == {0, 1, 2, 3}

    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert bfs(0, graph) == {0, 1}
    assert bfs(2, graph) == {2, 3}


def test_dfs():
    graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    assert dfs(0, graph) == {0, 1, 2}
    assert dfs(1, graph) == {0, 1, 2}

    graph = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
    assert dfs(0, graph) == {0, 1, 2, 3}
    assert dfs(3, graph) == {0, 1, 2, 3}

    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert dfs(0, graph) == {0, 1}
    assert dfs(2, graph) == {2, 3}


def test_empty_graph():
    graph = {}
    assert bfs(0, graph) == set()
    assert dfs(0, graph) == set()


def test_disconnected_graph():
    graph = {0: [1], 1: [0], 2: [3], 3: [2]}
    assert bfs(0, graph) == {0, 1}  # BFS starting at component 0
    assert bfs(2, graph) == {2, 3}  # BFS starting at component 2

    assert dfs(0, graph) == {0, 1}  # DFS starting at component 0
    assert dfs(2, graph) == {2, 3}  # DFS starting at component 2
