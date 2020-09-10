def bs(n, k, lo, hi):
    while lo <= hi: 
        mid = (hi + lo)//2
        summ = ((k * (k + 1))//2 - 1) - (((mid-1) * (mid))//2 -1) - (k-2)
        if summ == n: return k - mid + 1
        elif summ > n: lo = mid + 1            
        elif summ < n: hi = mid - 1
    if summ > n: mid += 1
    return k - mid + 1


def solve():
    n, k = map(int, input().split())
    if n == 1: return 0
    elif (k * (k + 1)//2) - (k-2) <= n: return -1
    elif k >= n: return 1
    else: return bs(n, k, 2, k)

print(solve())