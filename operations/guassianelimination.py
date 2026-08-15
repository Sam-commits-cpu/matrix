from operations.rowswap import row_swap_matrix
from operations.r_minus_kr import r_minus_kr_matrix


def guassian_elimination_matrix(A):
    found_pivot=False
    for current_row in range(len(A.data)):
        for current_col in range(len(A.data[0])):
            if current_row == current_col and (current_row+1)<=len(A.data):

                pivot=A.data[current_row][current_col]
                
                if pivot == 0  :
                    for temp_check_row in range(current_row,len(A.data)):

                        temp_pivot=A.data[temp_check_row][current_col]

                        if temp_pivot!=0:
                            A=row_swap_matrix(current_row,temp_check_row,A)
                            found_pivot=True
                            break

                    if not found_pivot:
                        continue          

                    pivot=A.data[current_row][current_col]



                for temp_row in range(current_row+1,len(A.data)):
                    k=A.data[temp_row][current_col]/pivot
                    A=r_minus_kr_matrix(
                        k,
                        temp_row,
                        current_row,
                        A
                    )

    return A
    


