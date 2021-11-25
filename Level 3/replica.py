def solution(x, y):
    
    x = int(x)
    y = int(y)
    moves = 0
    
    while (x > 1 and y > 1) or (x == 1 and y > 1) or (y == 1 and x > 1):
        if x > y:
            val = x - y 
            if val > y:
                rem = val % y
                val = val - rem
                moves = moves + (val/y)
                x = y + rem
            else:
                x = x - y
                moves = moves + 1
        elif y > x:
            val = y - x
            if val > x:
                rem = val % x
                val = val - rem
                moves = moves + (val/x)
                y = x + rem
            else:
                y = y - x
                moves = moves + 1
        else:
            break

    if x == 1 and y == 1:
        return str(moves)
    else:
        return ("impossible")
