from matrix import Matrix

def get_input():
    r = int(input("Enter no of rows : "))
    c = int(input("Enter no of columns : "))

    data = []

    for i in range(r):
        print(f"Enter values for row#{i+1} ---------------")

        temp_row = []

        for j in range(c):
            colvalue = int(input(f"col#{j+1} : "))
            temp_row.append(colvalue)

        data.append(temp_row)

    return Matrix(data)