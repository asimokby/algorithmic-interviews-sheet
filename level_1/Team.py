def solve():
    n = int(input())
    out = 0
    for i in range(n):
        if sum([int(j) for j in input().split()]) > 1:
            out += 1
    print(out)

solve()
