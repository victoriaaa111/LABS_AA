import time
import matplotlib.pyplot as plt
from decimal import Decimal, Context, ROUND_HALF_EVEN


# 1. recursive method
def fibonacci_recursive(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 2. dynamic method
def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


# 3. array method
def fibonacci_array(n):
    if n <= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            data.append(data[i - 1] + data[i - 2])
    return data[n - 1]


# 4. matrix method
def fibonacci_matrix(n):
    fib = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(fib, n - 1)
    return fib[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
        F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
        F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
        F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
        F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1], [1, 0]]
    for i in range(2, n + 1):
        multiply(F, M)


# 5. Binet Formula
def fibonacci_binet(n):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    phi = Decimal((1 + Decimal(5**(1/2))))
    phi2 = Decimal((1 - Decimal(5**(1/2))))
    return int((ctx.power(phi, Decimal(n)) - ctx.power(phi2,Decimal(n))) / (2**n * Decimal(5**(1/2))))


# 6. backtracking method
def fibonacci_backtracking(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci_backtracking(n - 1) + fibonacci_backtracking(n - 2)
        return memo[n]

