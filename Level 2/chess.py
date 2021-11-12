def solution(src, dest):
    
    def moveRightUp(src):
        dest = (src + 2)-8
        return dest
        
    def moveRightDown(src):
        dest = (src + 2) + 8
        return dest
        
    def moveUpRight(src):
        dest = (src - 16) + 1
        return dest
        
    def moveDownRight(src):
        dest = (src + 16) + 1
        return dest
        
    def moveLeftUp(src):
        dest = (src - 2) - 8
        return dest
        
    def moveLeftDown(src):
        dest = (src - 2) + 8
        return dest
        
    def moveUpLeft(src):
        dest = (src - 16) - 1
        return dest
        
    def moveDownLeft(src):
        dest = (src + 16) - 1
        return dest

    moves = []
    
    def checkKnight (src, dest, move):

        if src == dest:
            moves.append(0)

        if len(moves) == 0:
            factor = 100
        else:
            factor = min(moves)

        if move < factor:
            
            if src not in [0, 1, 2, 3, 4, 5, 6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55, 62, 63]:

                if moveRightUp(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveRightUp(src), dest, move+1)

            if src not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57]:
                    
                if moveLeftUp(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveLeftUp(src), dest, move+1)

            if src not in [56, 57, 58, 59, 60, 61, 62, 63, 6, 7, 14, 15, 22, 23, 30, 31, 38, 39, 46, 47, 54, 55]:

                if moveRightDown(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveRightDown(src), dest, move+1)

            if src not in [0, 1, 8, 9, 16, 17, 24, 25, 32, 33, 40, 41, 48, 49, 56, 57, 58, 59, 60, 61, 62, 63]:
                if moveLeftDown(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveLeftDown(src), dest, move+1)

            if src not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 23, 31, 39, 47, 55, 63]:

                if moveUpRight(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveUpRight(src), dest, move+1)

            if src not in [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 7, 15, 23, 31, 39, 47]:

                if moveDownRight(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveDownRight(src), dest, move+1)
                
            if src not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 24, 32, 40, 48, 56]:
                if moveUpLeft(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveUpLeft(src), dest, move+1)

            if src not in [0, 8, 16, 24, 32, 40, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]:
                if moveDownLeft(src) == dest:
                    moves.append(move)
                    return
                else:
                    checkKnight(moveDownLeft(src), dest, move+1)    

        return 

    checkKnight(src, dest, 1)
    return (min(moves)) 

print(solution(4,4))
  
