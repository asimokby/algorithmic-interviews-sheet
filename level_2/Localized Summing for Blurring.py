def rotate(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def cum_row(a):
    s, summ = [], 0
    for item in a:
        summ+= item
        s.append(summ)
    return s

def cum_cols(a):
    s = []
    for i  in rotate(a): s.append(cum_row(i))
    return rotate(s)

def sum_sub_mat(mat, n, m, i, j):
    top_left = mat[i-1][j-1] if i-1 > -1 and j-1 > -1 else 0
    top_right = mat[i-1][j+(m-1)] if i-1 > -1 else 0
    bottom_left = mat[i+(m-1)][j-1] if j-1> -1 else 0
    bottom_right = mat[i+(m-1)][j+(m-1)]
    return bottom_right + top_left - top_right - bottom_left

def print_result(res, n, m):
    summ = 0
    final = []
    res.reverse()
    for i in range((n-m)+1):
        for j in range((n-m)+1):
            summ += res[i][j]
            final.append(res[i][j])
    final.append(summ)
    return final

def solve():
    all_res = []
    next_ = input()
    while True: 
        try: 
            n, m = map(int, next_.split())
        except ValueError:
            next_ = input()
            if next_ == '': 
                break
            continue
        mat = []
        for _ in range(n): 
            row = []
            for _ in range(n): 
                row.append(int(input()))    
            mat.append(cum_row(row))
        mat.reverse()
        mat = cum_cols(mat) 
        res = []
        for i in range(n-m+1):
            res_row = []
            for j in range(n-m+1):
                res_row.append(sum_sub_mat(mat, n, m, i, j))
            res.append(res_row)
        res = print_result(res, n, m)
        all_res.append(res)
        try: next_ = input()
        except EOFError: break
    for idx, res in enumerate(all_res):
        for i in res:
            print(i)
        if idx != len(all_res)-1:
            print('')
solve()     