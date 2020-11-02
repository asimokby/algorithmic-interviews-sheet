def count_adj(idx, n, m, dictt, counted):
    right, left = idx+1, idx-1
    if idx % m == 0: right = -1
    elif idx % m == 1: left = -1 
    count, idxs = 0, [left, right, idx-m, idx+m]
    idxs = [i for i in idxs if i > 0 and i <= (n*m)]
    for i in idxs: 
        if dictt[i] != '.' and dictt[i] not in counted:
            count += 1
            counted.add(dictt[i])
    return count  

def solve():
    rw1 = input().split()
    n, m, c = int(rw1[0]), int(rw1[1]), rw1[2]
    dictt = {}
    idx = 1
    boss_idx = []  
    for _ in range(n):
        for elem in input():
            if elem == c: boss_idx.append(idx)
            dictt[idx] = elem
            idx+=1 
    res = 0
    counted = set([c])
    for bi in boss_idx: res+= count_adj(bi, n, m, dictt, counted)
    print(res)
solve()