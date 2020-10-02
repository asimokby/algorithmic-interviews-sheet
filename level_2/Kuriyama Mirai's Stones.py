def cum(a):
    s, summ = {}, 0
    for idx, item in enumerate(a):
        summ+= item
        s[idx] = summ
    return s

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    m = int(input())
    s, sorted_s = cum(a), cum(sorted(a))
    for _ in range(m):
        t, l, r = map(int, input().split())
        if t == 1: stype = s
        else: stype = sorted_s
        if l == 1: print(stype[r-1])
        else: print(stype[r-1] - stype[l-2])
solve()

   
