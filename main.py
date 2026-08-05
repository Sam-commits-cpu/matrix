from utils.input import get_input
from utils.display import print_matrix
from utils.display import end
from utils import validation
from operations.addition import add_matrices
from operations.multiplication import multi_matrices
from operations.transpose import transpose_matrix

#addition
def add_main():

    m1=get_input()
    m2=get_input()

    validation=validation.validate_add(m1,m2)
    if validation:
        print_matrix(m1.data)
        print_matrix(m2.data)
        m=add_matrices(m1,m2)
        print_matrix(m)
        end()
    else:
        end()

#multiplication
def multi_main():
    m1=get_input()
    m2=get_input()

    if validation.validate_multi(m1,m2):
        m=multi_matrices(m1,m2)
        print_matrix(m)
        end()
    else:
        end()

#transpose
def trans_main():
    m=get_input()
    print_matrix(m.data)

    AT=transpose_matrix(m)
    print_matrix(AT)

    end()

if __name__=="__main__":
    trans_main()