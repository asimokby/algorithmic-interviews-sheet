def top_sort(graph, visited, node, result):
    if node in visited: return
    visited.add(node) 
    for sub_node in graph[node]: top_sort(graph, visited, sub_node, result)
    result.append(node)

def solve():
    graph, visited, result =  {'A':[], 'B':[], 'C':[]}, set([]), []
    for _ in range(3):
        exp = input()
        if exp[1] == '<': graph[exp[2]].append(exp[0])
        else: graph[exp[0]].append(exp[2])
    if len([1 for i in graph.values() if len(i) > 0]) == 3: return 'Impossible'
    for node in graph: top_sort(graph, visited, node, result)
    return ''.join(result)

print(solve())
 