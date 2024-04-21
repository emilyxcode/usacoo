
# Calculate the nTH number(start from 0) in fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    print(f'n={n}; n-2={n - 2}; n-1={ n - 1}')
    left = fibonacci(n - 2)
    right = fibonacci(n - 1)
    ret =  left + right
    return ret

#0, 1, 1, 2, 3, 5, 8
print(fibonacci(3))
