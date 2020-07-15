def gcd(a, b):  # given a > b
    """
    Euclidean algorithm: 
    - example and a proof: https://www.youtube.com/watch?v=H_2_nqKAZ5w
    """
    while b:
        a, b = b, (a % b)
    return a

def solve():
    yak, wak = map(int, input().split())
    b = 7 - max(yak, wak)
    a = 6
    gcd_val = gcd(a, b)
    print(f'{b//gcd_val}/{a//gcd_val}')
solve()
