from utils.input import get_input

from utils.display import print_matrix
from utils.display import end

from utils import validation

from operations.addition import add_matrices
from operations.multiplication import multi_matrices
from operations.transpose import transpose_matrix
from operations.scalermultiplication import scaler_multi_matrix
from operations.identity import identity_matrix
from operations.zero import zero_matrix
from operations.trace import trace_matrix
from operations.determinant2x2 import det_2x2
from operations.determinant3x3 import det_3x3
from operations.determinantnxn import det_nxn
from operations.minor import minor_matrix
from operations.cofactor import cofactor_matrix
from operations.inverse2x2 import inverse_2x2_matrix
from operations.inversenxn import inverse_nxn_matrix
from operations.rowswap import row_swap_matrix
from operations.scalerrowmultiplication import scaler_row_multi_matrix
from  operations.r_plus_kr import r_plus_kr_matrix






####################### READ.ME ###################################
#                                                                 #
# Every Solution from module is a <Matrix instance>               #
# use result.data in  print_matrix() - send the data not instance #
# Always send instance during validation                          #
# All Modules - produces new matrix instances                     #
###################################################################

#addition
def add_main():

    m1=get_input()
    m2=get_input()

    validation=validation.validate_dimension(m1,m2)
    if validation:
        print_matrix(m1.data)
        print_matrix(m2.data)
        m=add_matrices(m1,m2)
        print_matrix(m.data )
        
        

#multiplication
def multi_main():
    m1=get_input()
    m2=get_input()

    if validation.validate_multi_dimension(m1,m2):
        m=multi_matrices(m1,m2)
        print_matrix(m.data)
        
        

#transpose
def trans_main():
    m=get_input()
    print_matrix(m.data)

    AT=transpose_matrix(m)
    print_matrix(AT.data)

    

#scaler multiplication
def scaler_multi_main():

    x=float(input("Enter lamda ::"))

    m=get_input()
    print_matrix(m.data)

    sm=scaler_multi_matrix(x,m)

    print_matrix(sm.data)

#creation of indentity matrix
def identity_main():

    i=int(input("Enter I :"))
    In=identity_matrix(i)
    print_matrix(In.data)
    

#creation of zero matrix
def zero_main():

    rows=int(input("Enter no of rows :"))
    cols=int(input("Enter no of columns :"))
    z=zero_matrix(rows,cols)
    print_matrix(z.data)

#matrix equality
def equality_main():
    A=get_input()
    B=get_input()

    print_matrix(A.data)
    print_matrix(B.data)

    #check dimension first 

    if validation.validate_dimension(A,B):
        if validation.validate_matrix_equality(A,B):
            print("Both are Same Matrices")
            
        else:
            print("Not Same Matrices")
         
        
#trace
def trace_main():

    x=get_input()
    print_matrix(x.data)

    if validation.validate_square_matrix(x):
        trace=trace_matrix(x.data)
        print(trace)    
        
    else:
        print("trace can't be calculated unless its a square matrix")
        
#diagonal matrix
def diagonal_main():

    x=get_input()
    print_matrix(x.data)
    if validation.validate_square_matrix(x):
        if validation.validate_diagonal_matrix(x):
            print("its diagonal matrix")
        else:
            print("its not diagonal")
    else:
        print('its not square')

#symmetric matrix
def symmetric_main():
    x=get_input()
    if validation.validate_square_matrix(x):
        xt=transpose_matrix(x)
        if validation.validate_matrix_equality(x,xt):
                print("Symmetric matrix")
        else:
                print("Not symmetric matrix")
    else:
        print("Not square matrix")
    
#skew-matrix AT=-A
def skew_main():
    A=get_input()
    AT=transpose_matrix(A)
    _A=scaler_multi_matrix(-1,A)
    if validation.validate_dimension(AT,_A) and validation.validate_matrix_equality(AT,_A):
        print("AT=-A")
    else:
        print("AT!=-A")


#upper-Trianglur matrix check 
#only elements below diagonal needs to be zero , doesn't matter if diagonal itself is zero
def upper_triangular_main():
    A=get_input()
    print_matrix(A.data)
    if validation.validate_upper_triangular_check_matrix(A) and len(A.data)==len(A.data[0]):
        print("its Upper_triangular_matrix")
    else:
        print("Not upper-triangular-matrix")

#lower-triangular matrix check
def lower_triangular_main():
    A=get_input()
    print_matrix(A.data)
    if validation.validate_lower_triangular_check_matrix(A) and len(A.data)==len(A.data[0]):
        print("its lower-triangular matrix")
    else:
        print("Not lower-triangular matrix")


#orthogonal matrix check ATxA=I
def orthogonal_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        AT=transpose_matrix(A)
        result=multi_matrices(A,AT)
        I=identity_matrix(len(A.data))
        if validation.validate_matrix_equality(result,I):
            print("It is a Orthogonal Matrix")
        else:
            print("It is Not")
    else:
        print("Enter a Square matrix")

#determinant-2x2 
def det_2x2_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        det=det_2x2(A)
        if det:
            print("det(a) :",det)
            print("Inverse Exist")
        else:
            print("det(a) : ",det)
            print("Inverse doesn't Exist")

#determinant-3x3
def det_3x3_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        det=det_3x3(A)
        if det:
            print("det(a) :",det)
        else:
            print("det(a) :",det)

#determinant-nxn
def det_nxn_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        det_A=det_nxn(A)
        print(f"det(A) : ",det_A)


#minor-matrix [m00...m22]
def minor_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        result=minor_matrix(A)
        if result:
            print_matrix(result.data) 
        else:
            print("")
    else:
        print("Not Square matrix")

#cofactor
#+-+,-+-,+-+
def cofactor_main():
    A=get_input()
    if validation.validate_square_matrix(A):
            mm=minor_matrix(A)
            if mm:
                print_matrix(mm.data)
                cofac=cofactor_matrix(mm)
                print_matrix(cofac.data) 
            else:
                print("")
    else:
            print("Not Square matrix")

#adjoint 
#transpose of cofactor of minor
def adjoint_main():
    A=get_input()
    if validation.validate_square_matrix(A):
            mm=minor_matrix(A)
            if mm:
                print_matrix(mm.data)
                cofac=cofactor_matrix(mm)
                print_matrix(cofac.data)
                trans=transpose_matrix(cofac)
                print_matrix(trans.data)

            else:
                print("")
    else:
            print("Not Square matrix")


#inverse main
#A^-1=(1/det(A))*adj(A)
#Adj(A)= cofactor matrix -> transpose
def inverse_2x2_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        print_matrix(A.data)
        a_inverse=inverse_2x2_matrix(A)
        if a_inverse:
            print_matrix(a_inverse.data)
        else:
            print()
    else:
        print("Not Square Matrix")

#inverse main for nxn
def inverse_nxn_main():
    A=get_input()
    if validation.validate_square_matrix(A):
        print_matrix(A.data)
        a_inverse=inverse_nxn_matrix(A)
        if a_inverse:
            print_matrix(a_inverse.data)
        else:
            print()
    else:
        print("Not a Square matrix")


#row swap
def row_swap_main():
    A=get_input()
    print_matrix(A.data)
    print("R1->0 R2->1 .......")
    f=int(input("Enter Row to be swaped ::"))
    s=int(input("Enter Row to be swaped with ::"))
    if f!=s:
        print(f"r{f+1} <----> r{s+1}")
        swap=row_swap_matrix(f,s,A)
        print_matrix(swap.data)
    else:
        print("Give different inputs")

#scaler row multiplication
def scaler_row_multi_main():
    A=get_input()
    scaler=float(input("Enter scaler ::"))
    rowno=int(input("Enter Index of row ::"))
    print_matrix(A.data)
    if  rowno<len(A.data):
        result=scaler_row_multi_matrix(scaler,rowno,A)

        print_matrix(result.data)
    else:
        print("Enter Valid Row Index")

#add multiple row to another
def r_plus_kr_main():
    A=get_input()
    row1=int(input("Enter r1 -> r1+kr2 => r1 :: "))
    scaler=float(input("Enter r1 -> r1+kr2 => k :: "))
    row2=int(input("Enter r1 -> r1+kr2 => r2 :: "))
    print_matrix(A.data)
    if row1<len(A.data):
        result=r_plus_kr_matrix(scaler,row1,row2,A)
        print_matrix(result.data)

    else:
        print("Enter Valid row-index")


if __name__=="__main__":
    r_plus_kr_main()
    end()