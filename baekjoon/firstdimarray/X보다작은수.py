def factorial_iterative(n):
    accum = n
    for i in range(n-1, 0, -1):
        accum *= i
        print(accum)
    print(accum)

    
    

factorial_iterative(5)