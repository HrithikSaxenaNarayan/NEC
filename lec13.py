def input_arr(n, val):
    if n == 0:
        return [0] * val

    arr = input_arr(n - 1, val)
    arr[n - 1] = int(input())

    return arr


def print_arr(arr, idx):
    if idx == len(arr):
        return

    print(arr[idx], end="\t")
    print_arr(arr, idx + 1)


def maximum(arr, idx):
    if idx == len(arr):
        return -10**9

    max_value = maximum(arr, idx + 1)

    return max(max_value, arr[idx])


def minimum(arr, idx):
    if idx == len(arr):
        return 10**9

    min_value = minimum(arr, idx + 1)

    return min(min_value, arr[idx])


def find(arr, idx, data):



n = int(input())
val = int(input())

arr = input_arr(n, val)

print_arr(arr, 0)
print()

print("Maximum:", maximum(arr, 0))
print("Minimum:", minimum(arr, 0))

data = int(input())

print("Found:", find(arr, 0, data))