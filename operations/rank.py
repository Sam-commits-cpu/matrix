def rank_matrix(A):
    a=A.data
    total_rank=0

    for row in range(len(a)):
        for col in range(len(a[0])):
            if a[row][col]!=0:
                total_rank+=1
                break

    return total_rank
                