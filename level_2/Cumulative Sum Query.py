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
    s = cum(a)
    for _ in range(m):
        l, r = map(int, input().split())
        if l == 0: print(s[r])
        else: print(s[r] - s[l-1])
solve()