def dfs(idx, i):
    if (idx < 0) or (idx == n) or (i < 0) or (i == n): return 
    if graph[idx][i] == 0 or (idx, i) in visited: return 
    visited.add((idx, i))
    #all eight directions
    dfs(idx, i-1) 
    dfs(idx, i+1)
    dfs(idx-1, i)
    dfs(idx-1, i+1)
    dfs(idx-1, i-1)
    dfs(idx+1, i)
    dfs(idx+1, i+1)
    dfs(idx+1, i-1)

def solve(graph, test_idx, dim):
    count = 0
    for idx, line in enumerate(graph):
        for i, node in enumerate(line):
            if node == 1 and (idx, i) not in visited:
                count += 1
                dfs(idx, i)
    print(f'Image number {test_idx} contains {count} war eagles.')

# taking input  
test_idx = 1
while True:
    graph = []
    visited = set()
    try: 
        n = int(input())
    except:
        break
    for _ in range(n):
        graph.append([int(i) for i in list(input())])
    solve(graph, test_idx, n)
    test_idx+=1

