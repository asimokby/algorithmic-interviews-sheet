from collections import defaultdict

def dfs(node, p_node, visited, graph):
    global length
    if visited[node]:
        return 'cycle'
    visited[node] = True
    for sub_node in graph[node]:
        if sub_node != p_node:
            length += 1
            if dfs(sub_node, node, visited, graph) == 'cycle':
                return 'cycle'


n, m = map(int, input().split())
visited = [None] + [False] * n
graph = defaultdict(lambda: [])
for _ in range(m):
    frm, to = map(int, input().split())
    graph[frm].append(to)
    graph[to].append(frm)

cycles = 0
for node in range(1, n+1):
    length = 0
    if not visited[node]:
        if dfs(node, 0, visited, graph) == 'cycle':
            cycles += (length % 2 == 1)

if (n-cycles) % 2 == 0:
    print(cycles)
else:
    print(cycles+1)
