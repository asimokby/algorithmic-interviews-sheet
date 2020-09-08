def solve():
    n, k = map(int, input().split())
    x = 0
    for _ in range(n):
        l, r = map(int, input().split())
        x += (r-l) + 1
    if x % k == 0: print(0)
    else: print(k - (x % k))
solve()