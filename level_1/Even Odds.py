def get_nth_even(n):
    return (n-1) * 2 + 2

def get_nth_odd(n):
    return (n-1) * 2 + 1
    
def solve():
    n, k = map(int, input().split())
    if n % 2 == 0:
        odd_ends_at = n//2
    else:
        odd_ends_at = n//2 + 1

    if k > odd_ends_at:
        print(get_nth_even(k-odd_ends_at))
    else:
        print(get_nth_odd(k))

solve()