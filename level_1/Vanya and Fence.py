def solve():
    n, h = map(int, input().split())
    heights = [int(i) for i in input().strip().split() if int(i) > h]

    print(n - len(heights) + len(heights) * 2)
solve()
