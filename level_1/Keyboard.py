def create_keyboard():
    keyboard = {}
    chars = '0qwertyuiop0asdfghjkl;0zxcvbnm,./0'
    for i in range(1, len(chars)-1):
        keyboard[chars[i]] = chars[i-1], chars[i+1]
    return keyboard

def solve():
    keyboard = create_keyboard()
    direc = 0 if input() == 'R' else 1
    new_s = []
    for i in input():
        new_s.append(keyboard[i][direc])
    print(''.join(new_s))

solve()

