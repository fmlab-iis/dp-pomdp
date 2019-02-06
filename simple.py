# to execute: do
# $ PYTHONPATH=<path to python Z3> python noisymax.py

from z3 import *
from matrix import *
from pufferfish import observationCheck, pufferfishCheck

rzero = RealVal (0)
rone = RealVal (1)

# (100/101)-geometric mechanism
GEOM = [[RealVal("10201/20301"), RealVal("100/20301"), RealVal("10000/20301")],
        [    RealVal("100/201"),     RealVal("1/201"),     RealVal("100/201")],
        [RealVal("10000/20301"), RealVal("100/20301"), RealVal("10201/20301")]]

# (9/10)-geometric mechanism
GEOM = [[RealVal("100/190"), RealVal("9/190"),  RealVal("81/190")],
        [   RealVal("9/19"),  RealVal("1/19"),    RealVal("9/19")],
        [ RealVal("81/190"), RealVal("9/190"), RealVal("100/190")]]

# (3/4)-geometric mechanism
GEOM = [[RealVal("16/28"), RealVal("3/28"),  RealVal("9/28")],
        [  RealVal("3/7"),  RealVal("1/7"),   RealVal("3/7")],
        [ RealVal("9/28"), RealVal("3/28"), RealVal("16/28")]]

GEOM = [[RealVal("2/3"), RealVal("1/6"),  RealVal("1/6")],
        [  RealVal("1/3"),  RealVal("1/3"),   RealVal("1/3")],
        [ RealVal("1/6"), RealVal("1/6"), RealVal("2/3")]]


def decode (n_queries, i):
    return [ int ((i / 3**q) % 3) for q in range (n_queries) ]

def encode (v):
    ret = 0
    for i in range (len (v) - 1, -1, -1):
        ret = ret * 3 + v[i]
    return ret

def argmax (l):
    ret = 0
    m = l[0]
    for i in range (len (l)):
        ret = i    if l[i] > m else ret
        m   = l[i] if l[i] > m else m
    return ret

def make_TR (n_queries):
    n_combs = 3 ** n_queries
    ret = mx_make (2 * n_combs, 2 * n_combs, rzero)
    for i in range (n_combs):
        v = decode (n_queries, i)
        for j in range (n_combs):
            vv = decode (n_queries, j)
            p = rone
            for q in range (n_queries):
                p = p * mx_get (GEOM, v[q], vv[q])
            mx_set (ret, i, n_combs + j, simplify (p))
    return ret

def make_OB (n_queries):
    n_combs = 3 ** n_queries
    ret = mx_make (2 * n_combs, n_queries + 1, rzero)
    for i in range (n_combs):
        mx_set (ret, i, n_queries, rone)
        v = decode (n_queries, i)
        idx = argmax (v)
        mx_set (ret, n_combs + i, idx, rone)
    return ret

def make_prior_dp (n_queries):
    n_combs = 3 ** n_queries
    pi = mx_make (2 * n_combs, 1, rzero)
    tau = mx_make (2 * n_combs, 1, rzero)
    ret = []
    for i in range (n_combs):
        v = decode (n_queries, i)
        p1 = 0.2
        p2 = 0.4
        temp1 = 1
        if v[0] == 0:
           temp1 *= (1-p1) ** 2
        elif v[0] == 1:
           temp1 *= 2*p1*(1-p1)
        else:
           temp1 *= p1 ** 2
        if v[1] == 0:
           temp1 *= (1-p2)
        elif v[1] == 1:
           temp1 *= 0
        else:
           temp1 *= p2
        temp2 = temp1
        if v[2] == 0:
           temp1 *= 0
           temp2 *= 0.5
        elif v[2] == 1:
           temp1 *= 0.5
           temp2 *= 0.5
        else:
           temp1 *= 0.5
           temp2 *= 0	
        mx_set (pi, encode (v), 0, temp1)	
        mx_set (tau, encode (v), 0, temp2)
    ret.append ((pi, tau))
    print (ret)
    return ret

n_queries = 3
TR = make_TR (n_queries)
OB = make_OB (n_queries)
dp_pairs = make_prior_dp (n_queries)
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)

s = Solver ()
s.add (observations)
s.push ()

for (pi, tau) in dp_pairs:
#    print (pi, tau)
    query = Or (
        pufferfishCheck (TR, OB, pi, tau, RealVal ("1/2"), ws),
        pufferfishCheck (TR, OB, tau, pi, RealVal ("1/2"), ws))
    s.add (query)
    result = s.check ()
    print (result)
    if result == sat:
        print (s.model ())
    s.pop ()
    s.push ()
