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

####################### READ.ME ###################################
#                                                                 #
# Every Solution from module is a <Matrix instance>               #
# use result.data in  print_matrix() - send the data not instance #
# Always send instance during validation                          #
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

    if len(x.data)==len(x.data[0]):
        trace=trace_matrix(x.data)
        print(trace)    
        
    else:
        print("trace can't be calculated unless its a square matrix")
        
#diagonal matrix
def diagonal_main():

    x=get_input()
    print_matrix(x.data)
    if len(x.data)==len(x.data[0]):
        if validation.validate_diagonal_matrix(x):
            print("its diagonal matrix")
        else:
            print("its not diagonal")
    else:
        print('its not square')

#symmetric matrix
def symmetric_main():
    x=get_input()
    if len(x.data)==len(x.data[0]):
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
    if len(A.data)==len(A.data[0]):
        AT=transpose_matrix(A)
        result=multi_matrices(A,AT)
        I=identity_matrix(len(A.data))
        if validation.validate_matrix_equality(result,I):
            print("It is a Orthogonal Matrix")
        else:
            print("It is Not")
    else:
        print("Enter a Square matrix")

if __name__=="__main__":
    orthogonal_main()
    end()