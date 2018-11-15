
from numpy import *

hh = .875
hl = .125
lh = .75
ll = .25

#survey query 0
"""
target = (' ', transpose (matrix (  (0, 1, 0, 0)  )))
P = dict ()
P['H'] = matrix (  ((0, hh, hl, 0),
                    (0,  1,  0, 0),
                    (0,  0,  1, 0),
                    (0, hl, hh, 0))  )
P['L'] = matrix (  ((0, lh, ll, 0),
                    (0,  1,  0, 0),
                    (0,  0,  1, 0),
                    (0, ll, lh, 0))  )
W = dict ()
W['H'] = dict ()
W['H']['*'] = matrix (  ((0, 0, 0, 0),
                         (0, 1, 0, 0),
                         (0, 0, 1, 0),
                         (0, 0, 0, 0))  )
W['L'] = dict ()
W['L']['*'] = W['H']['*']
"""

#survey query 1
"""
target = (' ', transpose (matrix (  (0, 1, 0, 0)  )))
P = dict ()
P['H'] = matrix (  ((0, hh, hl, 0),
                    (0,  1,  0, 0),
                    (0,  0,  1, 0),
                    (0, hl, hh, 0))  )
P['L'] = matrix (  ((0, lh, ll, 0),
                    (0,  1,  0, 0),
                    (0,  0,  1, 0),
                    (0, ll, lh, 0))  )
W = dict ()
W['H'] = dict ()
W['H']['Y'] = matrix (  ((0, 0, 0, 0),
                         (0, 1, 0, 0),
                         (0, 0, 0, 0),
                         (0, 0, 0, 0))  )
W['H']['N'] = matrix (  ((0, 0, 0, 0),
                         (0, 0, 0, 0),
                         (0, 0, 1, 0),
                         (0, 0, 0, 0))  )
W['L'] = dict ()
W['L']['Y'] = W['H']['Y']
W['L']['N'] = W['H']['N']
"""

#survey query 2
"""
target = (' ', transpose (matrix (  (1, 0)  )))
P = dict ()
P['H'] = matrix (  ((1, 0),
                    (0, 1))  )
P['L'] = P['H']

W = dict ()
W['H'] = dict ()
W['H']['Y'] = matrix (  ((hh,  0),
                         ( 0, hl))  )
W['H']['N'] = matrix (  ((hl,  0),
                         ( 0, hh))  )
W['L'] = dict ()
W['L']['Y'] = matrix (  ((lh,  0),
                         ( 0, ll))  )
W['L']['N'] = matrix (  ((ll,  0),
                         ( 0, lh))  )
"""

#survey with two queries
"""
target = (' ', transpose (matrix (  (0, 0, 0, 1, 0, 0, 0, 0)  )))

P = dict ()
P['H']  = matrix (  ((0, hh, hl,  0,  0,  0,  0,  0),
                     (0,  0,  0, hh, hl,  0,  0,  0),
                     (0,  0,  0, hh, hl,  0,  0,  0),
                     (0,  0,  0,  1,  0,  0,  0,  0),
                     (0,  0,  0,  0,  1,  0,  0,  0),
                     (0,  0,  0, hl, hh,  0,  0,  0),
                     (0,  0,  0, hl, hh,  0,  0,  0),
                     (0,  0,  0,  0,  0, hl, hh,  0))  )

P['L']  = matrix (  ((0, lh, ll,  0,  0,  0,  0,  0),
                     (0,  0,  0, lh, ll,  0,  0,  0),
                     (0,  0,  0, lh, ll,  0,  0,  0),
                     (0,  0,  0,  1,  0,  0,  0,  0),
                     (0,  0,  0,  0,  1,  0,  0,  0),
                     (0,  0,  0, ll, lh,  0,  0,  0),
                     (0,  0,  0, ll, lh,  0,  0,  0),
                     (0,  0,  0,  0,  0, ll, lh,  0))  )

W = dict ()
W['H'] = dict ()
W['H']['Y'] = matrix (  ((0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  1,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  1,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  1,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0))  )

W['L'] = dict ()
W['L']['Y'] = W['H']['Y']

W['H']['N'] = matrix (  ((0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  1,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  1,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  0,  0,  0,  0,  0,  1,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0))  )
W['L']['N'] = W['H']['N']
"""
"""
Gamma_2

H [[0.875 0.875 0.875 1.    0.    0.125 0.125 0.125]]
L [[0.875 0.75  0.75  1.    0.    0.25  0.25  0.125]]
H [[0.75  0.875 0.875 1.    0.    0.125 0.125 0.25 ]]
L [[0.75  0.75  0.75  1.    0.    0.25  0.25  0.25]]
"""

#survey with two queries but no observation

target = (' ', transpose (matrix (  (0, 0, 0, 1, 0, 0, 0, 0)  )))

P = dict ()
P['H']  = matrix (  ((0, hh, hl,  0,  0,  0,  0,  0),
                     (0,  0,  0, hh, hl,  0,  0,  0),
                     (0,  0,  0, hh, hl,  0,  0,  0),
                     (0,  0,  0,  1,  0,  0,  0,  0),
                     (0,  0,  0,  0,  1,  0,  0,  0),
                     (0,  0,  0, hl, hh,  0,  0,  0),
                     (0,  0,  0, hl, hh,  0,  0,  0),
                     (0,  0,  0,  0,  0, hl, hh,  0))  )

P['L']  = matrix (  ((0, lh, ll,  0,  0,  0,  0,  0),
                     (0,  0,  0, lh, ll,  0,  0,  0),
                     (0,  0,  0, lh, ll,  0,  0,  0),
                     (0,  0,  0,  1,  0,  0,  0,  0),
                     (0,  0,  0,  0,  1,  0,  0,  0),
                     (0,  0,  0, ll, lh,  0,  0,  0),
                     (0,  0,  0, ll, lh,  0,  0,  0),
                     (0,  0,  0,  0,  0, ll, lh,  0))  )

W = dict ()
W['H'] = dict ()
W['H']['*'] = matrix (  ((0,  0,  0,  0,  0,  0,  0,  0),
                         (0,  1,  0,  0,  0,  0,  0,  0),
                         (0,  0,  1,  0,  0,  0,  0,  0),
                         (0,  0,  0,  1,  0,  0,  0,  0),
                         (0,  0,  0,  0,  1,  0,  0,  0),
                         (0,  0,  0,  0,  0,  1,  0,  0),
                         (0,  0,  0,  0,  0,  0,  1,  0),
                         (0,  0,  0,  0,  0,  0,  0,  0))  )

W['L'] = dict ()
W['L']['*'] = W['H']['*']

"""
Gamma_2

H [[0.875 0.875 0.875 1.    0.    0.125 0.125 0.125]]
L [[0.875 0.75  0.75  1.    0.    0.25  0.25  0.125]]
H [[0.75  0.875 0.875 1.    0.    0.125 0.125 0.25 ]]
L [[0.75  0.75  0.75  1.    0.    0.25  0.25  0.25]]
"""

#survey with two queries by observation
"""
target = (' ', transpose (matrix (  (0, 0, 1, 0, 0, 0)  )))

P = dict ()
P['H']  = matrix (  ((0,  1,  0,  0,  0,  0),
                     (0,  0,  1,  0,  0,  0),
                     (0,  0,  0,  0,  0,  0),
                     (0,  0,  0,  0,  0,  0),
                     (0,  0,  0,  1,  0,  0),
                     (0,  0,  0,  0,  1,  0))  )

P['L']  = P['H']

W = dict ()
W['H'] = dict ()
W['H']['Y'] = matrix (  ((0,  0,  0,  0,  0,  0),
                         (0, hh,  0,  0,  0,  0),
                         (0,  0, hh,  0,  0,  0),
                         (0,  0,  0, hl,  0,  0),
                         (0,  0,  0,  0, hl,  0),
                         (0,  0,  0,  0,  0,  0))  )
W['H']['N'] = matrix (  ((0,  0,  0,  0,  0,  0),
                         (0, hl,  0,  0,  0,  0),
                         (0,  0, hl,  0,  0,  0),
                         (0,  0,  0, hh,  0,  0),
                         (0,  0,  0,  0, hh,  0),
                         (0,  0,  0,  0,  0,  0))  )

W['L'] = dict ()
W['L']['Y'] = matrix (  ((0,  0,  0,  0,  0,  0),
                         (0, lh,  0,  0,  0,  0),
                         (0,  0, lh,  0,  0,  0),
                         (0,  0,  0, ll,  0,  0),
                         (0,  0,  0,  0, ll,  0),
                         (0,  0,  0,  0,  0,  0))  )
W['L']['N'] = matrix (  ((0,  0,  0,  0,  0,  0),
                         (0, ll,  0,  0,  0,  0),
                         (0,  0, ll,  0,  0,  0),
                         (0,  0,  0, lh,  0,  0),
                         (0,  0,  0,  0, lh,  0),
                         (0,  0,  0,  0,  0,  0))  )
"""

def sum_of_product (P, W, v):
    ret = list ()
    for a in P.keys ():
        rv = transpose (matrix (zeros (v.size)))
        for w in W[a].keys ():
            rv += P[a] * W[a][w] * v
        ret.append ( (a, rv) )
    return ret

def collect_sop (Gamma):
    ret = list ()
    for i in Gamma:
        sop = sum_of_product (P, W, i[1])
        for rv in sop:
            ret.append (rv)
    return ret

def uniquify (Gamma):
    ret = []
    for i in Gamma:
        found = False
        for j in ret:
            if all (i[1] == j[1]):
                found = True
        if not found:
            ret.append (i)
    return ret

def print_sops (Gamma):
    for i in Gamma:
        print i[0], transpose (i[1])

Gamma_4 = [ target ]

print "Gamma_4\n"
print_sops (Gamma_4)

Gamma_3 = uniquify (collect_sop (Gamma_4))

print "\nGamma_3\n"
print_sops (Gamma_3)

Gamma_2 = uniquify (collect_sop (Gamma_3))

print "\nGamma_2\n"
print_sops (Gamma_2)

Gamma_1 = uniquify (collect_sop (Gamma_2))

print "\nGamma_1\n"
print_sops (Gamma_1)

Gamma_0 = uniquify (collect_sop (Gamma_1))

print "\nGamma_0\n"
print_sops (Gamma_0)

