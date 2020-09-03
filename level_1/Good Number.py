def solve():
    count = 0
    n, k = map(int, input().split())
    for _ in range(n):
        set_nums = set(input())
        good = True
        for i in range(k+1):
            if str(i) not in set_nums: good = False
        if good: count+=1 
    print(count)
solve()