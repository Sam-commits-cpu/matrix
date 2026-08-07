def trace_matrix(a):

    result = 0
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row==col:
                result+=a[row][col]

    return result