import math

def solution(n):
    return int(Q(n)-1)

def s(k):
        j = (0.5 + math.sqrt((0.5**2)-(4*1.5*(-k))))/(2*1.5)
        d = (0.5 - math.sqrt((0.5**2)-(4*1.5*(-k))))/(2*1.5)
        if j == int(j):
            return (-1)**j
        elif d == int(d):
            return (-1)**d
        else:
            return 0

qValues = [1]

def Q(n):

    if n <= len(qValues)-1:
        return qValues[n]
    else:
        sum = 0
        for i in range(1, int(math.sqrt(n))+1):
            sum = sum + (((-1)**(i+1))*(Q(n-(i*i))))
        fin = s(n) + 2*sum
        qValues.insert(n, fin)
        return fin

print(solution(200))





"""import itertools
from math import ceil

def solution(n):

    stairs = []
    numbers = [j for j in range (1, n+1)]

    for i in range(2, n+1):
        newStairs = list(itertools.combinations(numbers, i))
        stairs.extend(newStairs)

    print(len(stairs))
    final = []

    for stair in stairs:
        if sum(stair) == n:
            if stair not in final:
                final.append(stair)

    return print(len(final))

solution(12)"""