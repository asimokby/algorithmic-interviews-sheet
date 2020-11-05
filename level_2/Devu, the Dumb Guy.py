def solve():
    n, x = map(int, input().split())
    arr = [int(i) for i in input().split()]
    arr.sort()
    sum_ = 0
    for i in arr:
        sum_+= (i*x)
        if x > 1: x-=1
    print(sum_)
solve()
