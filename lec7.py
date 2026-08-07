def input2(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input())

    return arr

def lucky_number(arr):

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):

        min_value = arr[i][0]
        col = 0

        for j in range(1, cols):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                col = j

        lucky = True

        for k in range(rows):
            if arr[k][col] > min_value:
                lucky = False
                break

        if lucky:
            print(min_value)
            
            
def exit_point_of_matrix(arr):

    n = len(arr)
    m = len(arr[0])

    i = 0
    j = 0
    direction = 0

    while True:

        direction = (direction + arr[i][j]) % 4

        # East
        if direction == 0:
            j += 1
            if j == m:
                print(i, j - 1)
                break

        # South
        elif direction == 1:
            i += 1
            if i == n:
                print(i - 1, j)
                break

        # West
        elif direction == 2:
            j -= 1
            if j == -1:
                print(i, j + 1)
                break

        # North
        elif direction == 3:
            i -= 1
            if i == -1:
                print(i + 1, j)
                break
            
            
def diagonalDiff(arr):
    n = len(arr)
    m = 0
    k = 0
    
    for i in range(n):
        m += arr[i][i]
        k += arr[i][n - i - 1]
        
    return (m - k)