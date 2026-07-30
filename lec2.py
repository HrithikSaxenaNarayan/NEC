def reverse_order(n):
    while n != 0:
        ans = n % 10
        print(ans)
        n //= 10
        
        
def power(n):
    pow = 1
    while n != 0:
        n //= 10
        pow *= 10
    return pow // 10


def forward_order(n):
    pow = power(n)

    while n != 0:
        ans = n // pow
        print(ans)
        n %= pow
        pow //= 10