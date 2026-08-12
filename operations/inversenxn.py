from operations.determinantnxn import det_nxn
from operations.minor import minor_matrix
from operations.cofactor import cofactor_matrix
from operations.transpose import transpose_matrix
from operations.scalermultiplication import scaler_multi_matrix


def inverse_nxn_matrix(A):
    a=A.data
    det=det_nxn(A)
    if det==0:
        print()
        print("Inverse Doesnt Exist")
        return None
    divide1bydet=1/det

    minormatrix=minor_matrix(A)
    cofac=cofactor_matrix(minormatrix)
    adj=transpose_matrix(cofac)

    a_inverse=scaler_multi_matrix(divide1bydet,adj)

    return a_inverse

