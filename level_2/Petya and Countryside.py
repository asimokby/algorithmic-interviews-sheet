n = int(input())
recs = [int(i) for i in input().split()]

def neighbors(current, start, end, step):
    count = 0
    for j in range(start, end, step):
        if current >= recs[j]: 
            count += 1
            current = recs[j]
        else: return count
    return count


def solve():
    res = 1
    for i in range(n):
        maxx = 1
        current = recs[i]
        maxx += neighbors(current, i-1, -1, -1)
        maxx += neighbors(current, i+1, n, 1)
        if maxx > res: res = maxx
    print(res)
solve()