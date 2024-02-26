import math
from functools import reduce

def lcm(a, b):
    return a * b // math.gcd(a, b)

def solution(arr):
    return reduce(lcm, arr)
