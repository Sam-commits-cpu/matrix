
from operations.rowswap import row_swap_matrix
from operations.r_minus_kr import r_minus_kr_matrix
from operations.zero import zero_matrix
from operations.identity import identity_matrix
from utils.display import print_matrix


def LUdecomposition_matrix(inp_matrix):
    lena = len(inp_matrix.data)
    L = identity_matrix(lena)

    pivot_changed = False

    for current_row in range(lena):
        for current_col in range(lena):

            if current_row == current_col and (current_row + 1) <= lena:
                pivot = inp_matrix.data[current_row][current_col]
                print(f"Pivot :: {pivot}")

                if pivot == 0:
                    for check_pivot_row in range(current_row + 1, lena):
                        if inp_matrix.data[check_pivot_row][current_col] != 0:

                            for col in range(current_row):
                                L.data[current_row][col], L.data[check_pivot_row][col] = (
                                    L.data[check_pivot_row][col],
                                    L.data[current_row][col]
                                )

                            inp_matrix = row_swap_matrix(
                                current_row, check_pivot_row, inp_matrix
                            )

                            pivot = inp_matrix.data[current_row][current_col]
                            print("After swap ------------")
                            print_matrix(inp_matrix.data)
                            pivot_changed = True
                            break

                if pivot == 0:
                    print_matrix(inp_matrix.data)
                    raise ValueError(
                        "No nonzero pivot found; matrix is singular."
                    )

                for temp_pivot_row in range(current_row + 1, lena):
                    k = (
                        inp_matrix.data[temp_pivot_row][current_col] / pivot
                    )
                    print(
                        f"K : {k}="
                        f"{inp_matrix.data[temp_pivot_row][current_col]}/{pivot}"
                    )

                    L.data[temp_pivot_row][current_col] = k
                    inp_matrix = r_minus_kr_matrix(
                        k, temp_pivot_row, current_row, inp_matrix
                    )

                print("--------After elimination")
                print_matrix(inp_matrix.data)

            if pivot_changed:
                pivot_changed = False
                break
            else:
                if current_row < current_col:
                    L.data[current_row][current_col] = 0

    return L, inp_matrix
