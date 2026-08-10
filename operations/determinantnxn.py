from operations.determinant2x2 import det_2x2
from matrix import Matrix

def det_nxn(A):

    a=A.data
    n=len(a)
    total=0
    new_matrix,temp_row=[],[]

    if n==2:
        return det_2x2(A)
    
    for current_col in range(n):
            first_element=a[0][current_col]
            for row in range(n):
                if row==0:
                    continue
                for col in range(n):
                    if col==current_col:
                        continue
                    temp_row.append(a[row][col])
                new_matrix.append(temp_row)
                temp_row=[]
            new_A=Matrix(new_matrix)
            new_det=det_nxn(new_A)

            if current_col%2==0:
                total+=first_element*new_det
            else:
                total-=first_element*new_det
            new_matrix=[]
    return total


