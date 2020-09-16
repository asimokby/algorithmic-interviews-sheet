def solve():
    n, m = map(int, input().split())
    ab = []
    for _ in range(m): ab.append((tuple(map(int, input().split()))))
    put = 0
    for a, b in sorted(ab, key=lambda x: x[1], reverse=True):
        n -= a
        if n < 0: 
            put += (a+n) * b
            return put
        put += a * b
    return put
print(solve())
