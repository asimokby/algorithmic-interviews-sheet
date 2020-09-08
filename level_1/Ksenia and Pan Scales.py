def solve():
    left, right = input().split('|')
    b = input()
    diff = abs(len(left) - len(right)) 
    if not(len(b) >= diff and (len(b) - diff) % 2 == 0): return 'Impossible'
    each_len = (len(left) + len(right) + len(b))//2
    missing = abs(len(left)-each_len)
    return f"{''.join(left + b[:missing])}|{''.join(right + b[missing:])}"
print(solve())