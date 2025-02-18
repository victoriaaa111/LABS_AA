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

