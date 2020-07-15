def solve():
    s = list(input().strip())
    if sum([i.isupper() for i in s]) > len(s)//2:
        print(''.join(s).upper())
    else:
        print(''.join(s).lower())

solve()
