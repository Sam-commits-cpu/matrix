from operations.zero import zero_matrix
from utils.display import print_matrix


def Axb_extractor_matrix(matrix):

    a=matrix.data
    A=zero_matrix(len(a),len(a[0])-1)
    b=zero_matrix(len(a),1)
    rows=len(a)
    cols=len(a[0])

    #A
    for row in range(rows):
        for col in range(cols-1):
            A.data[row][col]=a[row][col]

    #b
    for xrow in range(rows):
        for ycol in range(cols-1,cols):
            b.data[xrow][0]=a[xrow][ycol]

    return A,b


    

