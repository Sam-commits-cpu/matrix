from matrix import Matrix
from operations.determinantnxn import det_nxn
from operations.zero import zero_matrix

def minor_matrix(A):

    a=A.data
    result_matrix=[]   
    zero_mat=zero_matrix(len(a),len(a[0])) #instance
    temp_row=[]

    if len(a)==1:
        zero_mat.data[0][0]=a[0][0]
        return zero_mat
    elif len(a)==2:
        zero_mat.data[0][0]=a[1][1]
        zero_mat.data[0][1]=a[1][0] 
        zero_mat.data[1][0]=a[0][1] 
        zero_mat.data[1][1]=a[0][0]
        return zero_mat


    for current_row in range(len(a)):
        for current_col in range(len(a[0])):
            for row in range(len(a)):
                if row == current_row:
                    continue
                for col in range(len(a[0])):
                    if col == current_col:
                        continue
                    temp_row.append(a[row][col])
                result_matrix.append(temp_row)
                temp_row=[]
            new_matrix=Matrix(result_matrix)    
            new_det=det_nxn(new_matrix)
            zero_mat.data[current_row][current_col]=new_det
            result_matrix=[]

    return zero_mat