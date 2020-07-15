from collections import defaultdict
def solve():
    n = int(input())
    t = input().split()
    t_freq = defaultdict(lambda: 0)
    t_idx = defaultdict(list)
    for idx, num in enumerate(t):
        t_freq[num] += 1
        t_idx[num].append(idx+1)

    if len(t_freq) == 3:
        min_t = min(t_freq.values())
        print(min_t)
        ts = list(t_idx.values())
        for i in range(min_t):
            print(f'{ts[0][i]} {ts[1][i]} {ts[2][i]}')
    else:
        print(0)

solve()
