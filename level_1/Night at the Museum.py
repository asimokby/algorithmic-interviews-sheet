def solve():
    cost = 0
    last_ch = 97
    for ch in input():
        clock_wise = abs(ord(ch) - last_ch)       
        cost += min(clock_wise, 26 - clock_wise)
        last_ch = ord(ch)
    print(cost)

solve()
