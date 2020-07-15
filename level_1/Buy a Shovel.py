def solve():
    k, r = map(int, input().split())
    shv = 1
    while True:
        if (shv * k % 10) == 0 or ((shv * k - r) % 10) == 0: 
            return shv
        shv += 1
print(solve())
