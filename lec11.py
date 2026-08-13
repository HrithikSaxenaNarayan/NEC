def array_lst_ops():
    arr_lst = []

    # Set or adding elements in the ArrayList
    arr_lst.append(10)
    arr_lst.append(int(input()))
    arr_lst.append(int(input()))
    arr_lst.append(40)

    print(arr_lst)

    # To know the length of the list
    print(len(arr_lst))

    # Get/render a particular element
    print(arr_lst[2])  # index starts from 0

    # Looping on the list
    for i in range(len(arr_lst)):
        print(arr_lst[i])

    # Or
    for elem in arr_lst:
        print(elem, end="\t")

    print()

    # To remove/delete element from the list
    arr_lst.pop(2)


def main():
    array_lst_ops()


main()