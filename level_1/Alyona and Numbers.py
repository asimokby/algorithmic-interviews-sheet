def solve():
    n, m = map(int, input().split())
    nn, mm = [0] * 5, [0] * 5
    for i in range(1, n+1):
        nn[i % 5] += 1
    for i in range(1, m+1):
        mm[i % 5] += 1
    print(nn[0]*mm[0] + nn[1]*mm[4] + nn[2]*mm[3] + nn[3]*mm[2] + nn[4]*mm[1])
solve()

