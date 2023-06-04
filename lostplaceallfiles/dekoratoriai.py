# from functools import wraps
# import math
#
#
# def limit_parameters(max_params):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if len(args) + len(kwargs) != max_params:
#                 raise ValueError("Incorrect number of parameters")
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @limit_parameters(2)
# def give_me_10():
#     """Grąžina skaičių 10"""
#     return 10
#
#
# @limit_parameters(2)
# def multiply(x, y):
#     return x * y
#
#
# @limit_parameters(3)
# def sum_all(a, b, c):
#     return a + b + c
#
#
# @limit_parameters(1)
# def square_root(x):
#     return math.sqrt(x)
#
#
# print(multiply(2, 3))
# print(sum_all(16, 200, 111))
# print(square_root(144))

##### 2 uzduotis ####
from time import sleep
from functools import wraps


def uzvelavimas(laikas):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                for letter in result:
                    sleep(laikas)
                    print(letter, end='', flush=True)
            return result

        return wrapper

    return decorator


@uzvelavimas(3)
def print_text():
    return "Cia rodau jums savo antra uzduoti."


print_text()
###### 3 uzduotis ####
# def tik_stringai(func):
#     def wrapper(*args):
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise ValueError("Funkcija priima tik string tipo parametrus")
#         return func(*args)
#     return wrapper
#
# @tik_stringai
# def example_function(text):
#     print("Pateiktas tekstas:", text)
#
# example_function("Ačiū")
# example_function("Hello")
# example_function(66688)
##### 4 uzduotis ####
# from time import time
# from functools import wraps
# import requests
#
# def fiksuoti_laika(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time()  # Fiksuojame starto laiką
#         result = func(*args, **kwargs)  # Iškviečiame originalią funkciją
#         end_time = time()  # Fiksuojame pabaigos laiką
#         execution_time = end_time - start_time  # Skaičiuojame vykdymo laiką
#
#         function_name = func.__name__
#         argument_values = ', '.join(repr(arg) for arg in args)
#         kwargs_values = ', '.join(f'{key}={repr(value)}' for key, value in kwargs.items())
#         all_arguments = ', '.join(filter(None, [argument_values, kwargs_values]))
#
#         print(f"Vykdymo laikas funkcijai {function_name}({all_arguments}): {execution_time:.2f} s")  # Atspausdiname vykdymo laiką
#         return result
#     return wrapper
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# @fiksuoti_laika
# def gauti_status_koda():
#     r = requests.get('http://www.cnn.com')
#     print("Statuso kodas:", r.status_code)
#     return r.status_code
#
#
# @fiksuoti_laika
# def rasti_pirminius_skaicius(*args):
#     pirminiai = []
#     for num in args:
#         if is_prime(num):
#             pirminiai.append(num)
#     print("Pirminiai skaičiai:", pirminiai)
#     return pirminiai
#
#
# gauti_status_koda()
# rasti_pirminius_skaicius(1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 13, 17 , 18 , 59, 60, 74, 109)
### info status kodai: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
