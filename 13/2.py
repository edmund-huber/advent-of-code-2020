#!/usr/bin/env python3
import collections
import copy
from functools import reduce

with open('input.txt') as f:
    ready_at = int(f.readline().rstrip())
    busses = []
    offs = []
    for i, id_ in enumerate(f.readline().rstrip().split(',')):
        if id_ != 'x':
            id_ = int(id_)
            busses.append(id_)
            offs.append(i)

print(busses)
print(offs)

rem = []
for bus, off in zip(busses, offs):
    rem.append(-off)
print(rem)

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(chinese_remainder(busses, rem))
