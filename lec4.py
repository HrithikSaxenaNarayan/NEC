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



