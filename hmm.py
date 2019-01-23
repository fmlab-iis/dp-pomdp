# to execute: do
# $ PYTHONPATH=<path to python Z3> python hmm.py

from sympy.interactive.printing import init_printing
init_printing()
from sympy.matrices import Matrix
from sympy import Rational, N
from z3 import *

TR = Matrix ([[Rational (2, 3), Rational (1, 6), Rational (1, 6)],
              [Rational (1, 3), Rational (1, 3), Rational (1, 3)],
              [Rational (1, 6), Rational (1, 6), Rational (2, 3)]])

# prior knowledge: family member, contagious disease

p0 = Matrix ([[1, 0, 0]])
p1 = Matrix ([[0, 0, 1]])

r0 = p0 * TR
r1 = p1 * TR

print (r0)
print (r1)

# prior knowledge: disease contraction rate is p, independent

rate = Real ('rate')
p_ind = Matrix ([[(1 - rate) * (1 - rate),
                  2 * rate * (1 - rate),
                  rate * rate]])
r_ = p_ind * TR
r_ind = [[r_[0].simplify (), r_[1].simplify (), r_[2].simplify ()]]

cond = 2 * rate * (1 - rate) + rate * rate
p_con = Matrix ([[0,
                  2 * rate * (1- rate) / cond,
                  rate * rate / cond]])
r__ = p_con * TR
r_con = [[r__[0].simplify (), r__[1].simplify (), r__[2].simplify ()]]

print r_ind
print r_con

solver = Solver ()
solver.add (0 <= rate)
solver.add (rate <= 1)
solver.push ()

print r_ind[0][0] <= 2 * r_con[0][0]
print r_con[0][0] <= 2 * r_ind[0][0]
solver.add (Not (And (
    rate**2/6 - 2*rate/3 + RealVal(2)/3 <= (-3*rate + 4)/(3*(-rate + 2)),
    (-3*rate + 4)/(6*(-rate + 2)) <= rate**2/3 - 4*rate/3 + RealVal(4)/3)))
if solver.check () == sat:
    print solver.model ()
    print ((lambda rate: N(rate**2/6 - 2*rate/3 + 2./3))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N((-3*rate + 4)/(3*(-rate + 2))))
           (solver.model ()[rate]))
    print "or"
    print ((lambda rate: N((-3*rate + 4)/(6*(-rate + 2))))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N(rate**2/3 - 4*rate/3 + 4./3))
           (solver.model ()[rate]))
else:
    print "pass"

solver.pop ()
solver.push ()
print r_ind[0][1] <= 2 * r_con[0][1]
print r_con[0][1] <= 2 * r_ind[0][1]
solver.add (Not (And (
    -rate**2/3 + rate/3 + RealVal(1)/6 <= (-3*rate + 4)/(3*(-rate + 2)),
    (-3*rate + 4)/(6*(-rate + 2)) <= -2*rate**2/3 + 2*rate/3 + RealVal(1)/3)))
if solver.check () == sat:
    print solver.model ()
    print ((lambda rate: N(-rate**2/3 + rate/3 + 1./6))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N((-3*rate + 4)/(3*(-rate + 2))))
           (solver.model ()[rate]))
    print "or"
    print ((lambda rate: N((-3*rate + 4)/(6*(-rate + 2))))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N(-2*rate**2/3 + 2*rate/3 + 1./3))
           (solver.model ()[rate]))
else:
    print "pass"
    
solver.pop ()
solver.push ()
print r_ind[0][2] <= 2 * r_con[0][2]
print r_con[0][2] <= 2 * r_ind[0][2]
solver.add (Not (And (
    rate**2/6 + rate/3 + RealVal(1)/6 <= 4/(3*(-rate + 2)),
    2/(3*(-rate + 2)) <= rate**2/3 + 2*rate/3 + RealVal(1)/3)))
if solver.check () == sat:
    print solver.model ()
    print ((lambda rate: N (rate**2/6 + rate/3 + 1./6))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N (4/(3*(-rate + 2))))
           (solver.model ()[rate]))
    print "or"
    print ((lambda rate: N (2/(3*(-rate + 2))))
           (solver.model ()[rate])), ">",
    print ((lambda rate: N (rate**2/3 + 2*rate/3 + 1./3))
           (solver.model ()[rate]))
else:
    print "pass"
    
