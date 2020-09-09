def solve():
    n = input()
    seq = input()
    for i in range(len(seq)-1):
        x, y = seq[i], seq[i+1]
        if x == '.' and y != '.': first_letter_idx = i+1
        if x != '.' and y == '.': last_letter_idx = i
        if x == 'R' and y == 'L': return f'{i+1} {i+2}'
    if seq[first_letter_idx] == 'R': return f'{first_letter_idx+1} {last_letter_idx+2}'
    return f'{last_letter_idx+1} {first_letter_idx}'
print(solve())  