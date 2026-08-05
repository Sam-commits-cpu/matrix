
def transpose_matrix(m):

    A=m.data

    result_matrix=[]
    temp_row=[]

    rows=len(A)
    cols=len(A[0])


    for row in range(cols):
            for col in range(rows):
                temp_row.append(A[col][row])
            result_matrix.append(temp_row)
            temp_row=[]


    return result_matrix

