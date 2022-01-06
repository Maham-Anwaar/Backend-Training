def prime_numbers(limit):
    for i in range(1, limit):
        is_prime = True
        for j in range(2, i-1):
            if i%j==0:
                is_prime = False
        if is_prime == True:
            print(" > ", i)

limit = int(input("Show me prime numbers up to .. ? "))
prime_numbers(limit)