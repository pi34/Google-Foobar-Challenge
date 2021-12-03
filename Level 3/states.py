from fractions import Fraction, gcd
import numpy as np


def decompose(m, terminals):

    q = []
    r = []

    for i in range(len(m)):
        if i not in terminals:
            currQ = []
            currR = []

            for j in range(len(m[i])):
                val = Fraction(m[i][j], (sum(m[i])))
                if j not in terminals:
                    currQ.append(val)
                else:
                    currR.append(val)
            q.append(currQ)
            r.append(currR)

    return (q, r)

    
def identity(n):
    return np.identity(n)


def subtract(m, j):
    m = np.array(m, dtype=Fraction)
    j = np.array(j, dtype=Fraction)
    return np.subtract(m, j)


def inverse(m):
    m = np.array(m, dtype='float')
    return np.linalg.inv(m)


def multiply(m, j):
    m = np.array(m, dtype=Fraction)
    j = np.array(j, dtype=Fraction)
    return np.dot(m, j)


def find_lcm(x, y):
    return abs(x*y) // gcd(x, y)


def returnLowForm(l):
    final = []

    num1 = Fraction(l[0]).limit_denominator().denominator
    num2 = Fraction(l[1]).limit_denominator().denominator

    lcm = find_lcm(num1, num2)

    for i in range(2, len(l)):
        lcm = find_lcm(lcm, Fraction(l[i]).limit_denominator().denominator)

    for r in l:
        div = lcm / Fraction(r).limit_denominator().denominator
        rN = Fraction(r).limit_denominator().numerator * div
        final.append(int(rN))

    final.append(lcm)
    return (final)
    
    
def solution(m):

    if len(m) == 1:
        return [1, 1]
        
    terminals = []
    
    for i in range(len(m)):
        if sum(m[i]) is 0:
            terminals.append(i)

    q, r = decompose(m, terminals)
    id = identity(len(q))
    sub = subtract(id, q)
    inv = inverse(sub)
    prob = multiply(inv, r)
    return (returnLowForm(prob[0]))
