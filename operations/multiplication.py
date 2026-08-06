from matrix import Matrix


def multi_matrices(a,b):

    m1,m2=a.data,b.data    
    result=0
    result_matrix,temp_row=[],[]
 

    for m1_row in range(len(m1)):
        for m2_col in range(len(m2[0])):
            for m2_row in range(len(m2)):
                result+= m1[m1_row][m2_row] * m2[m2_row][m2_col]
            temp_row.append(result)
            result=0
        result_matrix.append(temp_row)
        temp_row=[]


    return Matrix(result_matrix)