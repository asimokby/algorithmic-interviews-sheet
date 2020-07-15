def solve():
    n = input()
    res = sorted([int(i) for i in input().split()])
    print(' '.join(map(str, res)))


solve()
