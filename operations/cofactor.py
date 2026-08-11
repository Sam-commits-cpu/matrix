from matrix import Matrix 
from operations.zero import zero_matrix


#         ┌──────────────────┐
# A.data ─┤                  │
#         │  [[1, 2], [3,4]] │
# a ──────┤                  │
#         └──────────────────┘
# so making changes to "a" changes A.data - Thus i'm using zero-matrix

def cofactor_matrix(A):
    a=A.data

    zeromatrix=zero_matrix(len(a),len(a[0]))

    for row in range(len(a)):
        for col in range(len(a[0])):
            if (row+col) % 2 !=0:
                #odd+eve=odd
                zeromatrix.data[row][col]=-1*a[row][col]
            else:
                zeromatrix.data[row][col]=1*a[row][col]

    return zeromatrix