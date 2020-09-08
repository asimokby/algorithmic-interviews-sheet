from math import inf
def solve():
    n = int(input())
    movs = input()
    nums = [int(i) for i in input().split()]
    min_time = inf
    for i in range(len(movs)-1):
        if movs[i] == 'R' and movs[i+1] == 'L': 
            current_time = (nums[i+1] - nums[i])//2
            if current_time < min_time: min_time = current_time
    if min_time < inf: return min_time 
    return -1
print(solve())