
# (lru) = Least Recently Used Cache, provides a one line way to add memoization to your functions.
from functools import lru_cache

fib_cache = {}
natural_num_sum = {}


def factorial(n):
    """
    First recursive function

    Test Code:
    print(factorial(5))
    """

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n):
    """
    This function implements the famous number series (fibonacci) sequence without memory optimization
    or memoization.
    Test Code:
    print(fibonacci(7))

    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_opt(n):
    """
    This fibonacci function utilizes a programmable cache to optimize the efficiency of the functions
    run time. Mitigating repetitive calculations of base cases, the function can calculate much higher
    values for fibonacci sequence. additionally saves on overhead, more specifically memory overhead
    on recursive calls.

    Test Code:
    for i in range(1, 10001):
        print(i, ": ", fibonacci_opt(i))
    """
    if type(n) != int or n < 1:
        raise TypeError("n must be a positive integer")

    if n in fib_cache:
        return fib_cache[n]

    value = None
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n > 1:
        value = fibonacci_opt(n - 1) + fibonacci_opt(n - 2)

    fib_cache[n] = value
    return value


@lru_cache(maxsize=1000)
def fibonacci_opt2(n):
    """
    Does not seem to work currently. Need to find out why.

    Test Code:

    for i in range(1, 501):
        print(i, ": ", fibonacci_opt2(i))
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(n):
    """

    Test Code:
    print(" = ", sum_of_digits(123))
    """
    if n / 10 < 1:
        print(n, end=" ")
        return n
    print(n % 10, end=" + ")
    return n % 10 + sum_of_digits(n // 10)


def sum_of_natural_num(n):
    """
    This function sums the numbers of n natural numbers.
    Important to note that utilizing a stress test. The current implementation in this function
    fails when n = 998. RecursionError: maximum recursion depth exceeded in comparison.
    Thus, I will implement a function below which includes memoization to optimize the run time
    execution and compare test results.

    Test Code:
    for i in range(1, 101):
        print(i, ": ", sum_of_natural_num(i))

    """
    if n == 0:
        return 0

    return n + sum_of_natural_num(n - 1)


def sum_of_natural_num2(n):
    """
    Function works wonderfully, with memory optimization with a programmable cache implemented with a
    dictionary or make shift hash table.
    as constructed I tested this function up to n = 1,000,000, and it worked wonderfully. However, when
    n = 10,000,000, the function started to slow a little
    Test Code:
    for i in range(1, 1001):
        print(i, ": ", sum_of_natural_num2(i))

    """
    if type(n) != int or n < 0:
        raise TypeError("n must be a positive integer!")

    if n in natural_num_sum:
        return natural_num_sum[n]

    value = None
    if n == 0:
        value = 0
    elif n > 0:
        value = n + sum_of_natural_num2(n - 1)

    natural_num_sum[n] = value
    return value


def power_of_n(n, p):
    """
    Function computes an exponential power function for a given value. i.e. n^m, where n and m are
    members of the reals.

    Test Code:

    for i in range(1, 17):
        print("2^", i, ":", power_of_n(2, i))

    """
    if p == 0:
        return 1
    return n * power_of_n(n, p - 1)


for i in range(1, 17):
    print("2^", i, ":", power_of_n(2, i))






