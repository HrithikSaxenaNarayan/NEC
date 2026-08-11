def string_compression(string):
    n = len(string)
    i = 1
    ans = string[0]

    while i < n:
        while i < n and ans[-1] == string[i]:
            i += 1

        if i < n:
            ans += string[i]
            i += 1

    print(ans)


def string_compression_counts(string):
    n = len(string)
    i = 1
    count = 0
    ans = string[0]

    while i < n:
        count = 1

        while i < n and ans[-1] == string[i]:
            i += 1
            count += 1

        if count >= 1:
            ans = ans + ":" + str(count) + "\n"

        if i < n:
            ans += string[i]

        i += 1

    print(ans)


