def solve():
    num = input()
    res = ''
    for i in range(len(num)):
        temp = int(num[i])
        if temp >= 5 and not (9 - temp == 0 and i == 0): res+= str(9 - temp)
        else: res += str(num[i])
    print(res)
solve()
