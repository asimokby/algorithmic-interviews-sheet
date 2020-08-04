def dfs(graph, visited, dependent, node):
    if node in visited:
        return
    visited.add(node)
    for sub_node in graph[node]:
        dfs(graph, visited, dependent, sub_node)
    dependent.append(node)


def solve(graph, n):
    res, visited = [], set()
    for i in range(1, n + 1):
        i = str(i)
        dfs(graph, visited, res, i)
    print(' '.join(list(reversed(res))))


def take_input():
    while True:
        n, m = map(int, input().split())
        if n + m == 0: break
        graph = {str(k): [] for k in range(1, n + 1)}
        for _ in range(m):
            x, y = input().split()
            graph[x].append(y)
        solve(graph, n)

take_input()
