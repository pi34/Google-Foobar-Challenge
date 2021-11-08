from math import sqrt, ceil

def solution(i):
    # Your code here
    
    string = "2"
    
    for n in range(3, 50000):
        prime = True
        for z in range(2, ceil(sqrt(n))+1):
            if n % z == 0:
                prime = False
                
        if prime:
            string = string + str(n)
                
    return print(string[i : i+5])
    
solution(10000)