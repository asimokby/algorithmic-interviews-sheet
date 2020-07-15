import string
def solve():
    n, k = map(int, input().split())
    chrs = string.ascii_letters
    print(n//k * chrs[:k] + chrs[:n % k])
solve()
