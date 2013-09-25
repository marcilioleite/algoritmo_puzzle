'''
Created on 25/09/2013

@author: Marcilio
'''
def search(matrix, matching, row, col):
    
    matching.append([row,col])

    r1, c1 = (max(0, row-1), max(0, col-1))
    rn, cn = (min(len(matrix)-1, row+1), min(len(matrix[0])-1, col+1))
    
    for i in range(r1, rn+1):
        for j in range(c1, cn+1):
            
            equals   = matrix[i][j] == matrix[row][col]
            contains = [i,j] in matching 
            diagonal = i != row and j != col

            if (equals and not contains and not diagonal):
                search(matrix, matching, i, j)
    
