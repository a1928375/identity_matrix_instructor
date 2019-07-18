def is_identity_matrix(matrix):
    
    if len(matrix)==1:
        return False
        
    u=0
    for s in matrix:
        for t in s:
            if t<0:
                return False
            if t!=int(t):
                return False    

    for a in matrix:
        c=0
        for b in a:
            c=c+b
        if c!=1:
            return False
    
    i=0
    while i<len(matrix):
        j=0
        L=0
        while j<len(matrix):
            L=L+(matrix[j][i])
            j=j+1
        if L!=1:
            return False
        else:
            i=i+1
    
    return True



matrix = [[0,0.5,0.5],
           [0.5,0,0.5],
           [0.5,0.5,0]]
                      
print (is_identity_matrix(matrix))

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)

matrix6 = [[1,0,0,0],  
           [0,1,0,1],  
           [0,0,1,0],  
           [0,0,0,1]]

print is_identity_matrix(matrix6)

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)   
