from matrix import Matrix

def identity_matrix(i):

    result_matrix,temp_row=[],[]

    for row in range(i):
        for col in range(i):
            if row==col:
                result=1
            else:
                result=0
            temp_row.append(result)
        result_matrix.append(temp_row)
        temp_row=[]

    return Matrix(result_matrix)