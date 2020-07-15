def solve():
    n, x = map(int, input().split())
    distressed = 0
    for _ in range(n):
        op, num = input().split()
        if op == '+':
            x += int(num)
        else:
            if int(num) <= x:
                x -= int(num)
            else:
                distressed += 1
    print(x, distressed)


solve()
