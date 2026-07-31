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
        
        

