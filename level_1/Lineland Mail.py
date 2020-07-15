def solve():
    n = int(input())
    cities = [int(i) for i in input().split()]
    print(abs(cities[1] - cities[0]), abs(cities[0]-cities[-1]))
    for i in range(1, n-1):
        min_ = min(abs(cities[i]-cities[i+1]), abs(cities[i]-cities[i-1]))
        max_ = max(abs(cities[i]-cities[0]), abs(cities[i]-cities[n-1]))
        print(min_, max_)
    print(abs(cities[-1]-cities[-2]), abs(cities[0]-cities[-1]))
solve()
