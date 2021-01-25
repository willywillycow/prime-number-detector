def isprime(number):
    isprime = None
    for chosed in range(2, number):
        if number % chosed == 0:
            isprime = False
            break
        elif chosed == number - 1:
            isprime = True
    return isprime
