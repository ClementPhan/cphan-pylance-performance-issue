# Remove an intermediary step, put a list comprehension directly in for loop

from math import isnan
from typing import Callable


def linspace(start: float, stop: float, num: int = 50):
    if num == 1:
        yield stop
        return
    step = (stop - start) / (num - 1)
    for i in range(num):
        yield start + step * i


def find_zero(f: Callable[[float], float]):
    while True:
        if not(isnan(f_x_0)) and isnan(f_x_1):
            x_tests = list(linspace(x_1, x_0, 25))
            for x, f_x in zip(x_tests, (f(x) for x in x_tests)):
                if not(isnan(f_x)):
                    x_1 = x
                    f_x_1 = f_x
                    break

        elif isnan(f_x_0) and not(isnan(f_x_1)):
            x_tests = list(linspace(x_0, x_1, 25))
            for x, f_x in zip(x_tests, (f(x) for x in x_tests)):
                if not(isnan(f_x)):
                    x_0 = x
                    f_x_0 = f_x
                    break
