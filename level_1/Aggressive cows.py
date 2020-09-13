def valid(stalls, mid, c):
    cows_put, last_put_cow = 1, stalls[0]
    for i in range(1, len(stalls)):
            current = stalls[i]
            if current - last_put_cow >= mid:
                cows_put += 1
                if cows_put == c: return True
                last_put_cow = current
    return False 

def solve():
    for _ in range(int(input())): 
        n, c = map(int, input().split())
        stalls = [int(input()) for _ in range(n)]
        stalls.sort()
        lo, hi, res = 0, stalls[-1], 0 
        while lo <= hi: 
            mid = (lo + hi)//2
            if valid(stalls, mid, c): 
                lo = mid + 1
                if mid > res: res = mid
            else: hi = mid - 1
        print(res)
solve()
