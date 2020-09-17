def solve():
    n = input()
    count = 0 
    while len(n) > 1: 
        summ = 0
        for d in n: summ+= int(d)
        n = str(summ)
        count+=1
    print(count)
solve()