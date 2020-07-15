import re
def solve():
    print(len(set(re.split('[}{, ]', input()))) - 1) # -1 for the empty string
solve()
