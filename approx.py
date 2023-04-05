import math

def f(x):
    return 3 * x**2

def f_prime(x):
    return 6 * x

def f_3prime(x):
    return 0

def approx(x, h):
    return (1 / (2 * h)) * (4 * f(x + h) - 3 * f(x) - f(x + 2 * h))

h = 1
for x in range(0, 11):
    exact = f_prime(x)
    approx_val = approx(x, h)
    print('x = {}'.format(x))
    print('Exact: {}, Approx: {}'.format(exact, approx_val))
    print('Absolute error = {}'.format(abs(exact - approx_val)))
    print('Error Bound: {}'.format(f_3prime(x) * h**2 * 1/6))
    print()