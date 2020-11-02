def cum(a):
    s, summ = {}, 0
    for idx, item in enumerate(a):
        summ+= item
        s[idx] = summ
    return s


def solve():
    n, k = map(int, input().split())
    vals = [int(i) for i in input().split()]
    if k == n: return 1
    elif k == 1: return vals.index(min(vals)) + 1
    cum_vals = cum(vals)
    min_, min_idx, idx, came = cum_vals[k-1], 0, 0, False
    for i in range(k, n): 
        curr_min  = cum_vals[i] - cum_vals[idx]
        if curr_min < min_:
            min_ = curr_min     
            min_idx = idx
            came = True
        idx+=1
    if came: return min_idx+2
    return 1
print(solve())