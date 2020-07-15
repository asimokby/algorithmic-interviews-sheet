from collections import Counter

def solve():
    n = input()
    s = input().strip()
    freq = Counter(s)
    
    num_a_won = freq['A']
    num_d_won = freq['D']

    if num_a_won > num_d_won: print('Anton')
    elif num_a_won < num_d_won: print('Danik')
    else: print('Friendship')

solve()
