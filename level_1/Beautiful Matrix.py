def solve():
    for i in range(1, 6):
        row = input().split()
        position_1 = [(i, j) for j in range(1, 6) if row[j-1] == '1']
        if len(position_1) == 1:
            return abs(position_1[0][0] - 3) + abs(position_1[0][1] - 3)


res = solve()
print(res)
