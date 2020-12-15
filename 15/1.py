#!/usr/bin/env python3
import collections
import copy

def allindices(l, v):
    for i, v2 in enumerate(l):
        if v == v2:
            yield i

numbers = [1, 20, 11, 6, 12, 0]
turn = 0
while turn < 2020:
    print(numbers)
    if turn < len(numbers):
        pass
    else:
        num = numbers[-1]
        indices = list(allindices(numbers, num))
        if len(indices) == 1:
            numbers.append(0)
        elif len(indices) >= 2:
            numbers.append(indices[-1] - indices[-2])
        else:
            assert False
    turn += 1

print(turn)
print(numbers)
