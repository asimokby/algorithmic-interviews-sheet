def solve():
    n = int(input())
    coins = sorted((int(i) for i in input().split()), reverse=True)
    threshold = sum(coins)//2
    sum_ = 0    
    for idx, c in enumerate(coins):
        sum_ += c
        if sum_ > threshold:
            return idx + 1
print(solve())


