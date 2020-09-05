def hidden_nums():
    left, right = map(int, input().split())
    seen = set([left, right, 7-left, 7-right])
    hidden = [i for i in range(1, 7) if i not in seen]
    return hidden

def solve():
    n, top = int(input()), int(input())
    bottom = [7-top]
    for i in range(n):
        if top not in hidden_nums():
            return 'NO'
    return 'YES'
print(solve())