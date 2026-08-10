def validate_dimension(a,b):
    x=a.data
    y=b.data
    if len(x)==len(y):
        if len(x[0])==len(y[0]):
            return True
        else:
            print("xxx--- From validate_dimension ---xxx")
            print("xxx--- No.Columns aren't matching ---xxx")
            return False     
    else:
        print("xxx--- From validate_dimension ---xxx")
        print("xxx--- No.Rows aren't matching ---xxx")
        return False


def validate_multi_dimension(a,b):
    x=a.data
    y=b.data
    if (len(x)==len(y[0])) & (len(x[0])==len(y)):
        return True
    else:
        print(f"xxx--- From validate_multi_dimension ---xxx")
        print(f"xxx--- [A](ixj) != [B](jxi) ---xxx")
        return False

#needs rows x col need to be same
def validate_matrix_equality(A,B):
    a=A.data
    b=B.data
    for row in range(len(a)):
            for col in range(len(b[0])):
                        if a[row][col]!=b[row][col]:
                            return False
    return True

#send only square matrix
def validate_diagonal_matrix(A):
    A=A.data
    for row in range(len(A)):
        for col in range(len(A[0])):
            if A[row][col]!=0 and row!=col:
                 return False
    return True        


#upper-triangular matrix check
def validate_upper_triangular_check_matrix(A):
    a=A.data
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row>col and a[row][col]!=0:
                return False
    return True

 
#Lower-triangular matrix check
def validate_lower_triangular_check_matrix(A):
    a=A.data
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row<col and a[row][col]!=0:
                return False
    return True
     

