def solve():
    s = input()
    c = input()
    move = 0
    for i_c in range(len(c)):
        if c[i_c] == s[move]:
            move += 1
    print(move + 1)
solve()
    