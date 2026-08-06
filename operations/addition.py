from matrix import Matrix


def add_matrices(a, b):
    
    m1,m2=a.data,b.data
    result_matrix,temp_row = [],[]
    

    for row in range(len(m1)):
        for col in range(len(m1[0])):
            result = m1[row][col] + m2[row][col]
            temp_row.append(result)

        result_matrix.append(temp_row)
        temp_row = []

    return Matrix(result_matrix)