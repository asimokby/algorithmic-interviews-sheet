def solve():
    rows = []
    for _ in range(4): rows.append(input())
    for i in range(3):
        up, down = rows[i], rows[i+1]
        for j in range(4):
            x = up[j]
            if x == down[j]:
                if j == 0: 
                    if up[j+1] == x or down[j+1] == x: return 'YES'
                elif j == 3: 
                    if up[j-1] == x or down[j-1] == x: return 'YES'
                elif up[j-1] == x or up[j+1] == x or down[j-1] == x or down[j+1] == x: return 'YES'
    return 'NO'

print(solve())