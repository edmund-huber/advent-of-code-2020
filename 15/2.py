#!/usr/bin/env python3
import collections
import copy
import time

numbers = []
indices = collections.defaultdict(list)

def addnumber(num):
    global numbers
    global indices
    indices[num].append(len(numbers))
    numbers.append(num)

for num in [1, 20, 11, 6, 12, 0]:
    addnumber(num)

turn = 0
last= time.time()
while turn < 30000000:
    if turn % 1000000 == 0:
        now = time.time()
        print(now - last)
        last = now
    if turn < len(numbers):
        pass
    else:
        num = numbers[-1]
        idxs = indices[num]
        if len(idxs) == 1:
            addnumber(0)
        elif len(idxs) >= 2:
            addnumber(idxs[-1] - idxs[-2])
        else:
            assert False
    turn += 1

print(turn)
print(numbers[-1])
