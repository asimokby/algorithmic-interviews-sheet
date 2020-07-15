def solve():
    n = input()
    take_out = 0
    last_ch = None
    for ch in input():
        if ch == last_ch: take_out += 1
        last_ch = ch
    print(take_out)
    
solve()
