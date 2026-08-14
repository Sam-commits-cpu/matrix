from operations.zero import zero_matrix

def scaler_row_multi_matrix(scaler,Arow,A):
    a=A.data
    zero_mat=zero_matrix(len(a),len(a[0]))

    for row in range(len(a)):
        for col in range(len(a[0])):
            if row==Arow:
                zero_mat.data[row][col]=scaler * a[row][col]
            else:
                zero_mat.data[row]=a[row]

    return zero_mat