def solve():
    n = int(input())
    ns = [int(i) for i in input().split()]
    m = int(input())
    ms = [int(i) for i in input().split()]
    num_idx,left,right = {}, 0, 0
    for idx, num in enumerate(ns): num_idx[num] =  idx
    for q in ms:
        idx = num_idx[q]
        left += idx+1
        right += n - idx
    print(left, right)
solve()