def solve():
    n, k = (int(i) for i in input().split())
    s = (int(i) for i in input().split())
    count = 0
    for idx, score in enumerate(s):
        if idx == (k-1):
            k_score = score
        if score < k_score:
            break
        if score > 0:
            count += 1
    print(count)
solve()

