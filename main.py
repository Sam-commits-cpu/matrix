from utils.input import get_input
from utils.display import print_matrix
from utils.validation import validate_add
from operations.addition import add_matrices


def main():

    m1=get_input()
    m2=get_input()

    validation=validate_add(m1,m2)
    if validation:
        print_matrix(m1.data)
        print_matrix(m2.data)
        m=add_matrices(m1,m2)
        print_matrix(m)
        print("xxx----code ended ----xxx")
    else:
        print("xxx----code ended ----xxx")


if __name__=="__main__":
    main()