from matrix import Matrix

def zero_matrix(rows,cols):

    result_matrix,temp_row=[],[]

    for _ in range(rows):
        for _ in range(cols):
            temp_row.append(0)
        result_matrix.append(temp_row)
        temp_row=[]

    return Matrix(result_matrix)
    