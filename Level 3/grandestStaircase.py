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
