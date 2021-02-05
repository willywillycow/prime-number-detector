def isprime(number):
    isprime = None
    if number != 2:
        for chosed in range(2, number):
            if number % chosed == 0:
                isprime = False
                break
            elif chosed == number - 1:
                isprime = True
    elif number == 2:
        isprime = True
    return isprime
