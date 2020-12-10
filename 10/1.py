#!/usr/bin/env python3
import collections

jolts = []
with open('input.txt') as f:
    for line in f:
        jolts.append(int(line.rstrip()))

def pick(choices, chain, device_joltage):
    print(chain)
    print(len(jolts) - len(chain))
    print(device_joltage)
    if choices == set():
        if device_joltage == chain[-1] + 3:
            return chain + [device_joltage]
    solns = []
    for choice in choices:
        if 1 <= choice - (0 if chain == [] else chain[-1]) <= 3:
            res = pick(choices - set([choice]), chain + [choice], device_joltage)
            if res is not None:
                return res
    return None

assert len(set(jolts)) == len(jolts) # no dupes.
res = pick(set(jolts), [], max(jolts) + 3)
print('----')
print(res)

diffs = []
dist = collections.defaultdict(int)
for i, jolt in enumerate(res):
    if i == 0:
        diffs.append(jolt)
    else:
        diffs.append(res[i] - res[i-1])
    dist[diffs[-1]] += 1
print(diffs)
print(dist)

print(dist[1] * dist[3])
