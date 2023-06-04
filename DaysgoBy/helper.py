from functools import wraps
import math


def limit_parameters(max_params):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) + len(kwargs) != max_params:
                raise ValueError("Incorrect number of parameters")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@limit_parameters(2)
def multiply(x, y):
    return x * y


@limit_parameters(3)
def sum_all(a, b, c):
    return a + b + c


@limit_parameters(1)
def square_root(x):
    return math.sqrt(x)


print(multiply(2, 3))
print(sum_all(16, 200, 300))
print(square_root(144))
