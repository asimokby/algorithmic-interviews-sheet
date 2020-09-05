def is_valid(a, b, headers):
    r1, r2, c1, c2, d1, d2 = headers
    c, d = r1 - a, r2 - b
    res = [a, b, c, d]
    if a + d == d1 and b + c == d2 and len(res) == len(set(res)) and max(res) < 10:
        return res
    return -1

def print_result(res):
    if res == -1: 
        return 0
    print(res[0], res[2])
    print(res[1], res[3])
    return 1

def solve():
    r1, r2 = map(int, input().split()) 
    c1, c2 = map(int, input().split()) 
    d1, d2 = map(int, input().split())
    headers = [r1, r2, c1, c2, d1, d2]
    if not (r1 + r2 == c1 + c2 == d1 + d2): 
        print(-1)
        return
    for i in range(1, c1//2+1):
        if print_result(is_valid(i, c1-i, headers)) == 1: return
        if print_result(is_valid(c1-i, i, headers)) == 1: return 
    print(-1)
solve()