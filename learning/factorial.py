# write a function to calculate factorial

# n is a positive integer
def factorial(n):
    if n == 1:
        return 1
    temp = factorial(n - 1)
    return n * temp

print(factorial(3))

    
    
#f5 = factorial(5)