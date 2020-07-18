def solve():
    n = int(input())
    if n < 26:
        return 'NO'
    if len(set(input().lower())) == 26:
        return 'YES'
    return 'NO'
print(solve())