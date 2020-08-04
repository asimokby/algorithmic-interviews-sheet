from collections import defaultdict

def topological_sort(node, graph, visited, sorted_graph):
    if visited[node]:return
    visited[node] = True
    for sub_node in graph[node]:
        topological_sort(sub_node, graph, visited, sorted_graph)
    sorted_graph.append(node)


def solve():
    # input & graph
    sorted_graph = []
    n, k = map(int, input().split())
    visited = [None] + [False] * n
    graph = defaultdict(lambda: [])
    for i in range(1, k+1):
        graph[i] = [int(i) for i in input().split()][1:]
    # topological sort
    for node in range(1, n+1):
        if not visited[node] and node in graph:
            topological_sort(node, graph, visited, sorted_graph)
    # handle res
    res = [None] * (n + 1)
    last_superior = 0
    root = sorted_graph[-1]
    for node in reversed(sorted_graph):
        res[node] = last_superior
        if node <= k:
            last_superior = node

    for i in range(1, n+1):
        if res[i] == None:
            print(root)
        else:
            print(res[i])


solve()
