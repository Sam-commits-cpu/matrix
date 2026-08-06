from matrix import Matrix

def scaler_multi_matrix(x,m):

    matrix=m.data
    result_matrix,temp_row=[],[]
    result=1

    for row in range(len(matrix)):#rows
        for col in range(len(matrix[0])): #cols
            result*=x*matrix[row][col]
            temp_row.append(result)
            result=1
        result_matrix.append(temp_row)
        temp_row=[]


    return Matrix(result_matrix)