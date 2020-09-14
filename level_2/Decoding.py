def solve():
    n = int(input())
    s = [i for i in input()]
    indexes = []
    for i in range(n, 0, -1):
        if i % 2 == 0: add = -1
        else: add = len(indexes)
        indexes.append(i//2 + (add))
    print(''.join([i[1] for i in sorted(zip(indexes, s))]))
solve()