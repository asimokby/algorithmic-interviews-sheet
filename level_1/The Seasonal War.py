def look_around(x, idx, i):
    """
    This function could be implemented in a better way - the idea of 
    checking all the neighbors of a node could be handled in a better way 
    but this is fine.
    """
    around = set()
    up, down = (idx - 1 >= 0), (idx + 1 <= dim-1)
    left, right = (i - 1 >= 0), (i + 1 <= dim-1)
    if left:
        if x[idx][i-1] == 1: around.add((idx, i-1))
    if right:
        if x[idx][i+1] == 1: around.add((idx, i+1))
    if up: 
        if x[idx-1][i] == 1: around.add((idx-1, i))
        if right:
            if x[idx-1][i+1] == 1: around.add((idx-1, i+1))
        if left:
            if x[idx-1][i-1] == 1: around.add((idx-1, i-1))
    if down:
        if x[idx+1][i] == 1: around.add((idx+1, i))
        if right:
            if x[idx+1][i+1] == 1: around.add((idx+1, i+1))
        if left:
            if x[idx+1][i-1] == 1: around.add((idx+1, i-1))
    return around


def dfs(idx, i, node):
    if (idx, i) not in visited:
        visited.add((idx, i))
        neighbor_ones = look_around(graph, idx, i)
        for neighbor in neighbor_ones:
            dfs(neighbor[0], neighbor[1], graph[neighbor[0]][neighbor[1]])


def solve(graph, test_idx):
    count = 0
    for idx, line in enumerate(graph):
        for i, node in enumerate(line):
            if node == 1:
                if (idx, i) not in visited:
                    count += 1
                    dfs(idx, i, node)
    print(f'Image number {test_idx} contains {count} war eagles.')


# taking input  
test_idx = 1
while True:
    graph = []
    visited = set()
    try: 
        dim = int(input())
    except:
        break
    for _ in range(dim):
        graph.append([int(i) for i in list(input())])
    solve(graph, test_idx)
    test_idx+=1
