def solve(available_path, path):
    res = []
    for idx in range(len(available_path)-1):
        current_step = path[available_path[idx]]
        next_step = path[available_path[idx+1]]
        if current_step[0] == next_step[0]:
            if current_step[1] < next_step[1]:
                res.append('right')
            else:
                res.append('left')
        else:
            res.append('forth')
    return res

def take_input():
    available_path = '@IEHOVA#'
    for _ in range(int(input())):
        path = {}
        m, n = map(int, input().split())
        for i in range(m):
            line = input()
            for idx, ch in enumerate(line):
                if ch in available_path:
                    path[ch] = ((i, idx))
        res = solve(available_path, path)
        print(' '.join(res))

take_input()