def solve():
    for _ in range(int(input())):
        word = input()
        word_len = len(word)
        if word_len > 10:
            word = word[0] + str(word_len - 2) + word[-1]
        print(word)
solve()