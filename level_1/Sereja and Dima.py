def solve():
    n = input()
    cards = [int(i) for i in input().split()]
    leftmost = 0
    rightmost = len(cards) - 1
    turn = 0
    s = 0
    d = 0
    while rightmost >= leftmost:
        mx = max(cards[leftmost], cards[rightmost])
        # move pointers
        if mx == cards[leftmost]: leftmost += 1
        else: rightmost -= 1
        # handle turns
        if turn == 0:
            s += mx
            turn = 1
        else:
            d += mx
            turn = 0
    print(s, d)
solve()
