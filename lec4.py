def decimal_to_binary(n):
    ans = 0
    pow = 1

    while n != 0:
        rem = n % 2
        n //= 2
        ans += rem * pow
        pow *= 10

    return ans


# Example
n = 13
print(decimal_to_binary(n))  # Output: 1101