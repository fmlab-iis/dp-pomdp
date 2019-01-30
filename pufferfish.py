# to execute: do
# $ PYTHONPATH=<path to python Z3> python pufferfish.py

from sympy.interactive.printing import init_printing
init_printing()
from sympy.matrices import Matrix, zeros
from sympy import Rational, N
from z3 import *

rzero = RealVal (0)
rone = RealVal (1)
TR = Matrix (
    [[rzero, rzero, rzero, RealVal("2/3"), RealVal("1/6"), RealVal("1/6")],
     [rzero, rzero, rzero, RealVal("1/3"), RealVal("1/3"), RealVal("1/3")],
     [rzero, rzero, rzero, RealVal("1/6"), RealVal("1/6"), RealVal("2/3")],
     [rzero, rzero, rzero,          rzero,          rzero,          rzero],
     [rzero, rzero, rzero,          rzero,          rzero,          rzero],
     [rzero, rzero, rzero,          rzero,          rzero,          rzero]])

OB = Matrix ([[rzero, rzero, rzero,  rone],    # default observation
              [rzero, rzero, rzero,  rone],    # default observation
              [rzero, rzero, rzero,  rone],    # default observation
              [ rone, rzero, rzero, rzero],    # observe 0
              [rzero,  rone, rzero, rzero],    # observe 1
              [rzero, rzero,  rone, rzero]])   # observe 2


rate = Real ('rate')
a = Matrix ([[(1 - rate) * (1 - rate)],
             [2 * rate * (1 - rate)],
             [rate * rate],
             [rzero],
             [rzero],
             [rzero]])


pi  = Matrix ([[rone], [rzero], [rzero], [rzero], [rzero], [rzero]])
tau = Matrix ([[rzero], [rone], [rzero], [rzero], [rzero], [rzero]])

def select (v, vec):
    assert (vec.shape[1] == 1)
    size = vec.shape[0]
    ret = rzero
    for i in range (size - 1, -1, -1):
        ret = If (v == i, vec[i, 0], ret)
    return simplify (ret)

def dot (vec0, vec1):
    assert (vec0.shape[1] == 1)
    assert (vec1.shape[1] == 1)
    assert (vec0.shape[0] == vec1.shape[0])
    size = vec0.shape[0]
    ret = vec0[0, 0] * vec1[0, 0]
    for i in range (1, size):
        ret = vec0[i, 0] * vec1[i, 0] + ret
    print (ret)
    return simplify (RealVal (0) if ret == 0 else ret)

def sum (vec):
    assert (vec.shape[1] == 1)
    size = vec.shape[0]
    ret = vec[0, 0]
    for i in range (1, size):
        ret = vec[i, 0] + ret
    return ret

def pufferfishCheck (TR, OB, pi, tau, c, k):
    n_states = TR.shape[0]
    alpha = zeros (n_states, k)
    beta  = zeros (n_states, k)
    for s in range (n_states):
        w_0 = Int ('w_' + str (0))
        sel = select (w_0, OB.row (s).transpose ())
        alpha[s, 0] = pi[s] * select (w_0, OB.row (s).transpose ())
        beta[s, 0] = tau[s] * select (w_0, OB.row (s).transpose ())
    for t in range (1, k):
        w_t = Int ('w_' + str (t))
        for ss in range (n_states):
            x = dot (alpha.col(t-1), TR.col (ss))
            sel = select (w_t, OB.row (ss).transpose ())
#            print (x, sel)
            alpha[ss, t] = dot (alpha.col(t-1), TR.col (ss)) * sel
            beta[ss, t] = dot (beta.col(t-1), TR.col (ss)) * sel
    return sum (alpha.col (k-1)) > c * sum (beta.col (k-1))

print (pufferfishCheck (TR, OB, pi, tau, Q (2, 1), 2))


