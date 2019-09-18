def steps(number):
# Testing the collatz conjecture. Returns number of steps it takes, when dividing even numbers by 2 and multiplying odd numbers by 3 and adding 1.
    n = 0
    
    while number != 1:
        if number % 2 == 0:
            number = number/2
        else:
            number = number*3 + 1
        n = n + 1
    
    return(n)
