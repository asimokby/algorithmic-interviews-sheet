def solve():
    nums = sorted([int(i) for i in input().split('+')])
    print(''.join(([f'{i}+' for i in nums]))[:-1])
solve()
