
def mx_make (n_rows, n_cols, elm):
    row = [ elm for j in range (n_cols) ]
    return [ row.copy() for i in range (n_rows) ]

def mx_n_rows (mx) :
    return len (mx)

def mx_n_cols (mx) :
    return len (mx[0])

def mx_transpose (mx):
    n_rows = mx_n_rows (mx)
    n_cols = mx_n_cols (mx)
    return [ [ mx[i][j] for i in range (n_rows) ] for j in range (n_cols) ]

def mx_is_vector (mx) :
    return mx_n_cols (mx) == 1

def mx_row (mx, r) :
    return [ mx[r] ]

def mx_col (mx, c) :
    return [ [ mx[i][c] ] for i in range (mx_n_rows (mx)) ]

def mx_get (mx, r, c):
    return mx[r][c]

def mx_set (mx, r, c, elm):
    mx[r][c] = elm
