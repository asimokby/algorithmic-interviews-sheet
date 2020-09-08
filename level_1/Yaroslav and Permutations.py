from collections import Counter 
def solve():
    n = int(input())
    arr = input().split()
    freqs = Counter(arr)
    max_val_key = max(freqs, key=freqs.get)
    max_val = freqs[max_val_key]
    del freqs[max_val_key]
    if sum(freqs.values()) >= max_val - 1:
        print('YES')
    else: print('NO')
solve()