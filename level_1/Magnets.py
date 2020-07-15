def solve():
    n = int(input())
    groups = 0
    last_mg_x = None
    for i in range(n):
        x, _ = map(int, [i for i in input()])
        if last_mg_x != x: groups += 1
        last_mg_x = x
    print(groups)
solve()
