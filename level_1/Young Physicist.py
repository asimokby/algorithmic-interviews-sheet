def solve():
    x, y, z = 0, 0, 0
    for i in range(int(input())):
        a, b, c = [int(i) for i in input().strip().split()]
        x, y, z = x+a, y+b, z+c
    if all(v==0 for v in (x, y, z)):
        print('YES')
    else:
        print('NO')
solve()






# with numpy
import numpy as np
def solve():
    n = int(input())
    arr = np.zeros((n, 3))
    for i in range(n):
        arr[i] = [int(i) for i in input().strip().split()]
    if np.any(np.sum(arr, axis=0)):
        print('NO')
    else:
        print('YES')
# solve()
