import time
import matplotlib.pyplot as plt
from decimal import Decimal, Context, ROUND_HALF_EVEN
from tabulate import tabulate
import sys

sys.setrecursionlimit(16000)


# 1. recursive method
def fibonacci_recursive(nr):
    if nr <= 0:
        print("Incorrect input")
    elif nr == 1:
        return 0
    elif nr == 2:
        return 1
    else:
        return fibonacci_recursive(nr - 1) + fibonacci_recursive(nr - 2)


# 2. dynamic method
def fibonacci_dynamic(nr):
    fib = [0, 1]
    for i in range(2, nr + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[nr]


# 3. backtracking with memorization method
def fibonacci_backtracking(nr, memo={}):
    if nr <= 0:
        return 0
    elif nr == 1:
        return 1
    elif nr in memo:
        return memo[nr]
    memo[nr] = fibonacci_backtracking(nr - 1, memo) + fibonacci_backtracking(nr - 2, memo)
    return memo[nr]


# 4. matrix method
def fibonacci_matrix(nr):
    fib = [[1, 1], [1, 0]]
    if nr == 0:
        return 0
    power(fib, nr - 1)
    return fib[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, nr):
    M = [[1, 1], [1, 0]]
    for i in range(2, nr + 1):
        multiply(F, M)


# 5. Binet Formula
def fibonacci_binet(nr):
    ctx = Context(prec=60, rounding=ROUND_HALF_EVEN)
    phi = Decimal((1 + Decimal(5**(1/2))))
    phi2 = Decimal((1 - Decimal(5**(1/2))))
    return int((ctx.power(phi, Decimal(nr)) - ctx.power(phi2, Decimal(nr))) / (2**nr * Decimal(5**(1/2))))


# 6. iterative method
def fibonacci_iterative(nr):
    a, b = 0, 1
    for _ in range(nr):
        a, b = b, a + b
    return a


# measure time
def measure_time(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    return result, end_time - start_time


# inputs
input_1 = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
input_2 = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

results = {method.__name__: {'values': [], 'times': []} for method in
           [fibonacci_recursive, fibonacci_dynamic, fibonacci_backtracking, fibonacci_matrix, fibonacci_binet,
            fibonacci_iterative]}


for n in input_1:
    _, time_taken = measure_time(fibonacci_recursive, n)
    results['fibonacci_recursive']['times'].append(time_taken)

for n in input_2:
    for method in [fibonacci_dynamic, fibonacci_backtracking, fibonacci_matrix, fibonacci_binet, fibonacci_iterative]:
        _, time_taken = measure_time(method, n)
        results[method.__name__]['times'].append(time_taken)


# plot all methods
for method_name, data in results.items():
    plt.figure(figsize=(10, 6))
    if method_name == 'fibonacci_recursive':
        plt.plot(input_1, data['times'], marker='o', label=method_name, color='m')
        for n, time_taken in zip(input_1, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)
    else:
        plt.plot(input_2, data['times'], marker='o', label=method_name, color='m')
        for n, time_taken in zip(input_2, data['times']):
            plt.text(n, time_taken, f'{time_taken:.4f} sec', ha='right', va='bottom', fontsize=8)

    plt.title(f'Execution Time for {method_name} Method')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (seconds)')
    plt.yscale('log')
    plt.legend()
    plt.grid(True)

plt.show()

# print results for recursive
recursive_table = [["n", "Time (seconds)"]]
for n, time_taken in zip(input_1, results['fibonacci_recursive']['times']):
    recursive_table.append([n, f"{time_taken:.6f}"])

print("\nRecursive Method Results:")
print(tabulate(recursive_table, headers="firstrow", tablefmt="grid"))

# print results for other methods
methods = ['fibonacci_dynamic', 'fibonacci_backtracking', 'fibonacci_matrix', 'fibonacci_binet', 'fibonacci_iterative']
methods_table = [["n"] + methods]

for i, n in enumerate(input_2):
    row = [n] + [f"{results[m]['times'][i]:.6f}" for m in methods]
    methods_table.append(row)

print("\nOther Methods Results:")
print(tabulate(methods_table, headers="firstrow", tablefmt="grid"))
