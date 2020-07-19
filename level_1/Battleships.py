def dfs(graph, i, j, n, visited):
    if i < 0 or i == n or j < 0 or j == n: return 
    if graph[i][j] == '.' or (i, j) in visited: return 
    visited.add((i, j))
    dfs(graph, i-1, j, n, visited) #up
    dfs(graph, i+1, j, n, visited) #down
    dfs(graph, i, j+1, n, visited) #right
    dfs(graph, i, j-1, n, visited) #left

def solve(graph, n, test_num):
    visited = set()
    count = 0
    for i, line in enumerate(graph):
        for j, ch in enumerate(line):
            if graph[i][j] == 'x' and (i, j) not in visited:
                dfs(graph, i, j, n, visited)
                count += 1
    print(f'Case {test_num}: {count}')

def take_input():
    for test_num in range(1, int(input())+1):
        graph = []
        n = int(input())
        for i in range(n):
            graph.append(list(input()))
        solve(graph, n, test_num)

take_input()

