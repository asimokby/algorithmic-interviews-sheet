def solve():
    x = 0
    for _ in range(int(input())):
        op = input()
        if op[1] == '+':
            x += 1
        else:
            x -= 1
    print(x)
solve()
