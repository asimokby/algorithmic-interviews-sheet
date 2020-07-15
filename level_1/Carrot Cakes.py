#explaination
# 1) number of time segments t that cover time segment d, say x
# 2) total time of the segments covering the time segment d, say y
# 3) get the number of rounds you need to bake a k cakes, say z
# 4) if the time y is equal to d, and there is more than 1 round print(yes)
# 5) if the time y is more than d(cant be smaller than d), and there is 1 or more rounds print(yes)
# 6) else print(no)

import math
def solve():
    n, t, k, d = map(int, input().split())
    x = math.ceil(d/t) 
    y = int(x * t) 
    rounds_needed = 0 
    if d == y: rounds_needed = 1
    group_ks = math.ceil(n/k)
    if group_ks - x > rounds_needed:
        print('YES')
    else:
        print('NO')
solve()
