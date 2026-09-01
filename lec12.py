def input_map(n):
    map_data = {}

    for i in range(n):
        map_data[i] = int(input())

    return map_data


def display(map_data):
    for key, value in map_data.items():
        print(f"{key}: {value}")


def display_gen(map_data):
    for key, value in map_data.items():
        print(f"{key}: {value}")


def arr_to_map(n):
    arr = []

    for i in range(n):
        arr.append(int(input()))

    return arr


def count_freq(arr):
    map_data = {}

    for i in range(len(arr)):
        value = arr[i]

        if value in map_data:
            map_data[value] += 1
        else:
            map_data[value] = 1

    return map_data


# main
n = int(input())

display_gen(count_freq(arr_to_map(n)))