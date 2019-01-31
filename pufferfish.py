
from z3 import *

rzero = RealVal (0)
rone = RealVal (1)

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

def observationCheck (OB, ws):
    ret = True
    for w_t in ws:
        ret_t = False
        for i in range (mx_n_cols (OB)):
            ret_t = Or (ret_t, w_t == i)
        ret = And (ret, ret_t)
    return simplify (ret)
    
def select (v, vec):
    assert (mx_is_vector (vec))
    size = mx_n_rows (vec)
    ret = rzero
    for i in range (size - 1, -1, -1):
        ret = If (v == i, mx_get (vec, i, 0), ret)
    return simplify (ret)

def dot (vec0, vec1):
    assert (mx_is_vector (vec0))
    assert (mx_is_vector (vec1))
    assert (mx_n_rows (vec0) == mx_n_rows (vec1))
    size = mx_n_rows (vec0)
    ret = rzero
    for i in range (0, size):
        ret = mx_get (vec0, i, 0) * mx_get (vec1, i, 0) + ret
    return simplify (ret)

def sum (vec):
    assert (mx_is_vector (vec))
    size = mx_n_rows (vec)
    ret = rzero
    for i in range (0, size):
        ret = mx_get (vec, i, 0) + ret
    return simplify (ret)

def pufferfishCheck (TR, OB, pi, tau, c, ws):
    n_states = mx_n_rows (TR)
    n_obs = mx_n_cols (OB) # the default observation must be the last
    alpha = mx_make (n_states, len (ws), rzero)
    beta  = mx_make (n_states, len (ws), rzero)
    w_0 = ws[0]
    for s in range (n_states):
        sel = select (w_0, mx_transpose (mx_row (OB, s)))
        mx_set (alpha, s, 0, simplify (mx_get (pi,  s, 0) * sel))
        mx_set (beta,  s, 0, simplify (mx_get (tau, s, 0) * sel))
    for t in range (1, len (ws)):
        w_t = ws[t]
        for ss in range (n_states):
            x = dot (mx_col (alpha, t-1), mx_col (TR, ss))
#            print (mx_col (alpha, t-1), mx_col (TR, ss))
            sel = select (w_t, mx_transpose (mx_row (OB, ss)))
            mx_set (alpha, ss, t,
                    dot (mx_col (alpha, t-1), mx_col (TR, ss)) * sel)
            mx_set (beta,  ss, t,
                    dot (mx_col (beta,  t-1), mx_col (TR, ss)) * sel)
                            
    distinguish = (    sum (mx_col (alpha, len (ws) - 1)) >
                   c * sum (mx_col (beta, len (ws) - 1)))
    return simplify (distinguish)



