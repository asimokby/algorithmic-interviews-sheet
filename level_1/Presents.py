def solve():
    n = input()
    ps = input().split()
    ps = [(int(ps[i]), i+1) for i in range(len(ps))]
    print(' '.join([str(i[1]) for i in sorted(ps)]))
solve()
