def odd_left_even_right(arr):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] *= -1

    arr.sort()

    idx = 0
    while idx < len(arr) and arr[idx] < 0:
        arr[idx] *= -1
        idx += 1

    return arr