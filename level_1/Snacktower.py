def solve():
    n = int(input())
    waiting_for = n
    stored = set([])
    for i in [int(i) for i in input().split()]:
        if i == waiting_for:
            stored.add(i)
            res = []
            for j in range(i, 0, -1):
                if j in stored: 
                    res.append(str(j))
                else:
                    waiting_for = j
                    break
            print(' '.join(res))
        else:
            print('')
            stored.add(i)
solve()

