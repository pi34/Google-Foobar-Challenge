import itertools

def solution(num_buns, num_required):
    # Your code here
    
    NumberEachKey = 1 + num_buns - num_required
    finalArr = [[] for i in range(num_buns)]
    
    combin = list(itertools.combinations(range(num_buns), NumberEachKey))
    for keyCurr, bunnies in enumerate(combin):
        for i in bunnies:
            finalArr[i].append(keyCurr)
            
    return finalArr
