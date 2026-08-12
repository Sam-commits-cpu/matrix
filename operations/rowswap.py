from operations.zero import zero_matrix

def row_swap_matrix(f,s,A):
    a=A.data
    zero_mat=zero_matrix(len(a),len(a[0]))
    zero_mat.data[f],zero_mat.data[s]=a[s],a[f]
    for row in range(len(a)):
        if row==f or row==s:
            continue
        zero_mat.data[row]=a[row]
    return zero_mat