def solve():
    n, l = map(int, input().split())
    lans = sorted([int(i) for i in input().split()])
    left, right, diff = lans[0] - 0, l - lans[-1], 0
    for i in range(1, len(lans)):
        curr = lans[i] - lans[i-1]
        if curr > diff: diff = curr

    print(max(left, right, diff/2))

solve()
         

    