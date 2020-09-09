def bs(arr, q, lo, hi):
    mid = (hi - lo)//2 + lo
    if q == arr[mid]: return mid-1, mid+1
    elif lo >= hi: 
        if q > arr[lo]: return lo, lo+1
        else: return lo-1, lo
    elif q < arr[mid]: return bs(arr, q, lo, mid-1)
    elif q > arr[mid]: return bs(arr, q, mid+1, hi)
    

def solve():
    _ = int(input())
    arr = list(dict.fromkeys([int(i) for i in input().split()]))
    _ = int(input())
    qs = [int(i) for i in input().split()]
    n = len(arr)
    for q in qs:
        x = bs(arr, q, 0, n-1)
        res = []
        if x[0] > -1: res.append(str(arr[x[0]]))
        else: res.append('X')
        if x[1] < n: res.append(str(arr[x[1]]))
        else: res.append('X')
        print(' '.join(res))

solve()
