def solve():
    n = int(input()) 
    rem, s, rem_s = n%4, 'GBIV', ''
    if rem: rem_s = s[:rem]
    print('ROY' + (n//4 * s)[3:] + rem_s)
solve() 
