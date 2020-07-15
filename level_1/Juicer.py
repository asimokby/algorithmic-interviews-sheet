def solve():
    n, b, d = map(int, input().split())
    sizes = [int(i) for i in input().split()]

    juc = 0
    waste = 0
    for s in sizes:
        if s <= b:
            juc += s
        if juc > d:
            juc = 0
            waste += 1

    print(waste)
solve() 
