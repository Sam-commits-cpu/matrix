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

####################### README ##################################
#                                                                #
# Every Solution from module is a <Matrix instance>              #
# use result.data in  print_matrix() - send the data not instance#
# Always send instance during validation                         #
#################################################################

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
        end()
    else:
        end()

#multiplication
def multi_main():
    m1=get_input()
    m2=get_input()

    if validation.validate_multi_dimension(m1,m2):
        m=multi_matrices(m1,m2)
        print_matrix(m.data)
        end()
    else:
        end()

#transpose
def trans_main():
    m=get_input()
    print_matrix(m.data)

    AT=transpose_matrix(m)
    print_matrix(AT.data)

    end()

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
    end()

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
            end()
        else:
            print("Not Same Matrices")
            end()
    else:
        end()

    


if __name__=="__main__":
    equality_main()