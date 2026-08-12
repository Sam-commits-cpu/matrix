from operations.determinant2x2 import det_2x2
from operations.cofactor import cofactor_matrix
from operations.transpose import transpose_matrix
from operations.scalermultiplication import scaler_multi_matrix
from operations.minor import minor_matrix

def inverse_2x2_matrix(A):

        det=det_2x2(A)
        if det==0:
            print()
            print("Inverse Doesn't Exist")
            return None    
        divide1bydet=1/det

        minormatrix=minor_matrix(A)
        cofac=cofactor_matrix(minormatrix)
        adj=transpose_matrix(cofac)
        
        a_inverse=scaler_multi_matrix(divide1bydet,adj)
        
        return a_inverse

