# to execute: do
# $ PYTHONPATH=<path to python Z3> python pufferfish.py

from z3 import *
from pufferfish import observationCheck, pufferfishCheck

rzero = RealVal (0)
rone = RealVal (1)

TR = [[rzero, rzero, rzero, RealVal("2/3"), RealVal("1/6"), RealVal("1/6")],
      [rzero, rzero, rzero, RealVal("1/3"), RealVal("1/3"), RealVal("1/3")],
      [rzero, rzero, rzero, RealVal("1/6"), RealVal("1/6"), RealVal("2/3")],
      [rzero, rzero, rzero,          rzero,          rzero,          rzero],
      [rzero, rzero, rzero,          rzero,          rzero,          rzero],
      [rzero, rzero, rzero,          rzero,          rzero,          rzero]]

OB = [[rzero, rzero, rzero,  rone],    # default observation
      [rzero, rzero, rzero,  rone],    # default observation
      [rzero, rzero, rzero,  rone],    # default observation
      [ rone, rzero, rzero, rzero],    # observe 0
      [rzero,  rone, rzero, rzero],    # observe 1
      [rzero, rzero,  rone, rzero]]   # observe 2

pi   = [[rone],  [rzero], [rzero], [rzero], [rzero], [rzero]]
tau0 = [[rzero],  [rone], [rzero], [rzero], [rzero], [rzero]]
tau1 = [[rzero], [rzero],  [rone], [rzero], [rzero], [rzero]]

s = Solver ()
s.push ()
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)
example1 = Or (pufferfishCheck (TR, OB, pi, tau0, RealVal (2), ws),
               pufferfishCheck (TR, OB, tau0, pi, RealVal (2), ws))
#print (example1)
s.add (observations)
s.add (example1)
print (s.check ())
s.pop ()

s.push ()
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)
example2 = Or (pufferfishCheck (TR, OB, pi, tau1, RealVal (2), ws),
               pufferfishCheck (TR, OB, tau1, pi, RealVal (2), ws))
#print (example2)
s.add (observations)
s.add (example2)
print (s.check ())
print (s.model ())
s.pop ()

s.push ()
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)
#print (observations)
rate = Real ('rate')
pi_ind = [[(1 - rate) * (1 - rate)],
          [2 * rate * (1 - rate)],
          [rate * rate],
          [rzero],
          [rzero],
          [rzero]]
cond0 = (2 * rate * (1 - rate)) + rate * rate
tau_cond0 =  [[rzero],
              [2 * rate * (1 - rate)/cond0],
              [rate * rate/cond0],
              [rzero],
              [rzero],
              [rzero]]
example40 = Or (pufferfishCheck (TR, OB, pi_ind, tau_cond0, RealVal (2), ws),
                pufferfishCheck (TR, OB, tau_cond0, pi_ind, RealVal (2), ws))
#print (example40)
s.add (And (0 < rate, rate < 1))
s.add (observations)
s.add (example40)
print (s.check ())
s.pop ()

s.push ()
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)
cond1 = (1 - rate) * (1 - rate) + 2 * rate * (1 - rate)
tau_cond1 = [[(1 - rate) * (1 - rate)/cond1],
             [2 * rate * (1 - rate)/cond1],
             [rzero],
             [rzero],
             [rzero],
             [rzero]]
example41 = Or (pufferfishCheck (TR, OB, pi_ind, tau_cond1, RealVal (2), ws),
                pufferfishCheck (TR, OB, tau_cond1, pi_ind, RealVal (2), ws))
s.add (And (0 < rate, rate < 1))
s.add (observations)
s.add (example41)
print (s.check ())
s.pop ()

s.push ()
ws = [ Real ('w_' + str (t)) for t in range (2) ]
observations = observationCheck (OB, ws)
rate0 = Real ('rate0')
rate1 = Real ('rate1')
rate2 = Real ('rate2')
pi_all = [[rate0], [rate1], [rate2], [rzero], [rzero], [rzero]]
tau_all0 = [[rzero], [rate1/(rate1 + rate2)], [rate2/(rate1+rate2)],
            [rzero],                 [rzero],               [rzero]]
example50 = And (
    Not (pufferfishCheck (TR, OB, pi_all, tau_all0, RealVal (2), ws)),
    Not (pufferfishCheck (TR, OB, tau_all0, pi_all, RealVal (2), ws)))
s.add (And (0 < rate0, rate0 < 1))
s.add (And (0 < rate1, rate1 < 1))
s.add (And (0 < rate2, rate2 < 1))
s.add (rate0 + rate1 + rate2 == 1)
s.add (observations)
s.add (example50)
tau_all1 = [[rate0/(rate0+rate1)], [rate1/(rate0 + rate1)], [rzero],
            [rzero],                 [rzero],               [rzero]]
example51 = And (
    Not (pufferfishCheck (TR, OB, pi_all, tau_all1, RealVal (2), ws)),
    Not (pufferfishCheck (TR, OB, tau_all1, pi_all, RealVal (2), ws)))
s.add (ws[0] == 3)
s.add (example51)
print (s.check ())
print (s.model ())
