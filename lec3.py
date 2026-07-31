def binomial_pattern(num):
    for n in range(num):
        nCr = 1

        for r in range(n + 1):
            print(nCr, end="\t")
            nCr1 = ((n - r) * nCr) // (r + 1)
            nCr = nCr1

        print()
        
