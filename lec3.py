def binomial_pattern(num):
    for n in range(num):
        nCr = 1

        for r in range(n + 1):
            print(nCr, end="\t")
            nCr1 = ((n - r) * nCr) // (r + 1)
            nCr = nCr1

        print()
        

def num_pattern4(n):
    nsp = n - 1
    nst = 1

    for row in range(1, n + 1):

        for _ in range(nsp):
            print("\t", end="")

        val = row
        for cst in range(1, nst + 1):
            print(val, end="\t")

            if cst <= nst // 2:
                val += 1
            else:
                val -= 1

        nsp -= 1
        nst += 2
        print("\t")

def numW(n):
    nst = 1
    nsp = (2 * n) - 3

    for row in range(1, n + 1):
        val = 1

        # Left side
        for _ in range(nst):
            print(val, end="\t")
            val += 1

        # Spaces
        for _ in range(nsp):
            print(end="\t")

        # Right side
        for cst in range(1, nst + 1):
            if row == n and cst == 1:
                val -= 1
                continue
            val -= 1
            print(val, end="\t")

        nst += 1
        nsp -= 2
        print()
        
        

