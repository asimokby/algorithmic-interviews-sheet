n, c = map(int, input().split())
cts = [int(i) for i in input().split()]

def solve():
    if n < 2 or n == c: return sum(cts) 
    ones, doubts = 1 if cts[c-1] == 1 else 0, 0
    for i in range(c, n):
        curr, mirror_dist = cts[i],  c-(i - c + 1)-1 
        if curr == 1: ones += 1
        if mirror_dist > -1:
            if curr == 1 and cts[mirror_dist] == 1: ones += 1
            elif curr == 1 and cts[mirror_dist] == 0: doubts += 1
            elif curr == 0 and cts[mirror_dist] == 1: 
                ones += 1
                doubts += 1      
    if mirror_dist > 0: return sum(cts[:mirror_dist]) + ones - doubts
    return ones - doubts

print(solve())