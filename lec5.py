def input_matrix(n, m):
    arr = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input()))
        arr.append(row)

    return arr


def display(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()


# Main
n = int(input())
m = int(input())

matrix = input_matrix(n, m)
display(matrix)