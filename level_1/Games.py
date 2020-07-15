from collections import defaultdict

def solve():
    n = int(input())
    h_d = defaultdict(lambda: 0)
    a_d = defaultdict(lambda: 0)
    for i in range(n):
        h, a = map(int, input().split())
        h_d[h] += 1
        a_d[a] += 1
    res = 0
    for k in h_d:
        res += h_d[k] * a_d[k]
    print(res)
solve()
