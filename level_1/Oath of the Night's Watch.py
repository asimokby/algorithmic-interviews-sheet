def solve():
    n = int(input())
    x = sorted([int(i) for i in input().split()])
    min_, max_ = x[0], x[-1]
    count = 0
    for i in x:
        if i > min_ and i < max_:
            count +=1 
    print(count)
solve()
