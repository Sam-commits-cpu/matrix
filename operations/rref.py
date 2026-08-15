from operations.scalerrowmultiplication import scaler_row_multi_matrix
from operations.r_minus_kr import r_minus_kr_matrix

from utils.display import print_matrix


#only works when converting ref - > rref from gaussian elimination

def backward_elimination_matrix(A):

    print(f"original matrix")
    print_matrix(A.data)


    for current_col in range(len(A.data[0])-1,-1,-1):
        for current_row in range(len(A.data)-1,-1,-1):

            print(f"({current_row},{current_col})")

            if current_row == current_col :
                pivot=A.data[current_row][current_col]
                print(f"current_row==current_col :  ({current_row},{current_col}) , pivot : {pivot}")

                if pivot!=0:
                    if pivot!=1:
                        temp_pivot=1/pivot

                        temp_operation_matrix=scaler_row_multi_matrix(
                            temp_pivot,
                            current_row,
                            A
                        )
                        A=temp_operation_matrix
                        print(f"temp_pivot :{temp_pivot} , current_row : {current_row} ")
                        print_matrix(A.data)

                    for temp_row in range(current_row - 1, -1, -1):
                    
                        k=A.data[temp_row][current_col]
                        r_minus_kr_result_matrix=r_minus_kr_matrix(k,temp_row,current_row,A)
                        A=r_minus_kr_result_matrix

                        print()
                        print(f"performing zero operation :: in the specific col ({temp_row},{current_col})")
                        print_matrix(A.data)    

            
    print(f"Final matrix ------------------")
    print_matrix(A.data)
    return A
                