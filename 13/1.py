#!/usr/bin/env python3
import collections
import copy

with open('input.txt') as f:
    ready_at = int(f.readline().rstrip())
    busses = f.readline().rstrip().split(',')
    busses = list(filter(lambda x: x != 'x', busses))
    busses = [int(x) for x in busses]

print(ready_at)

soonest = None
soonest_at = None
for bus in busses:
    print(bus)
    print(ready_at % bus)
    if ready_at % bus == 0:
        soonest = bus
        soonest_at = 0
    else:
        new_soonest_at = bus - (ready_at % bus)
        if soonest is None or new_soonest_at < soonest_at:
            soonest = bus
            soonest_at = new_soonest_at

print(soonest * soonest_at)
