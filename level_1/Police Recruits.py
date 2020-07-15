def solve():
    n = input()
    events = map(int, input().split())
    crime = 0
    free = 0
    for ev in events:            
        if ev > 0: free += ev
        else:
            if free > 0: free -= 1
            else: crime += 1
    print(crime)
    
solve()
