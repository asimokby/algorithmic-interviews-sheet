def solve():
    c = list(map(int, input().split()))
    wasted_c = 0
    for ch in input(): 
        wasted_c += c[int(ch) - 1]
    print(wasted_c)
solve()