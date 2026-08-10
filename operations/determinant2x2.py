#only square matrix
def det_2x2(A):
    a=A.data
    ad=a[0][0] * a[1][1]
    cb=a[0][1] * a[1][0]
    return ad - cb