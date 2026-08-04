def decimal_to_binary(n):
    ans = 0
    pow = 1

    while n != 0:
        rem = n % 2
        n //= 2
        ans += rem * pow
        pow *= 10

    return ans



def binary_to_decimal(n):
    pwr = 1
    ans = 0

    while n != 0:
        rem = n % 10
        ans += rem * pwr
        pwr *= 2
        n //= 10

    return ans


def add_two_arrays(arr, brr):
    n = len(arr)
    m = len(brr)

    ans_len = max(n, m) + 1
    ans = [0] * ans_len

    i = n - 1
    j = m - 1
    k = ans_len - 1
    carry = 0

    while k >= 0:
        total = carry

        if i >= 0:
            total += arr[i]

        if j >= 0:
            total += brr[j]

        carry = total // 10
        ans[k] = total % 10

        i -= 1
        j -= 1
        k -= 1

    
    start = 1 if ans[0] == 0 else 0

    for idx in range(start, ans_len):
        print(ans[idx], end="\t")
