from operations.scalerrowmultiplication import scaler_row_multi_matrix
from operations.zero import zero_matrix

def r_plus_kr_matrix(scaler,r1,kr2,A):
    a=A.data
    kr2_mat=scaler_row_multi_matrix(scaler,kr2,A)
    temp_row=kr2_mat.data[kr2]
    zero_mat=zero_matrix(len(a),len(a[0]))

    
    for row in range(len(a)):
        for col in range(len(a[0])):

            if row==r1:
                zero_mat.data[row][col]= a[row][col] + temp_row[col]
            else:
                zero_mat.data[row]=a[row]
    return zero_mat