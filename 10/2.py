#!/usr/bin/env python3
import collections

jolts = []
with open('input.txt') as f:
    for line in f:
        jolts.append(int(line.rstrip()))

def ass():
    #print(chain)
    #print(len(jolts) - len(chain))
    if chain != [] and target_joltage == chain[-1] + 3:
        return [chain + [target_joltage]]
    solns = []
    for choice in choices:
        if 1 <= choice - (start_joltage if chain == [] else chain[-1]) <= 3:
            print(chain)
            print(start_joltage)
            print(choice)
            solns.extend(pick(choices - set([choice]), start_joltage, chain + [choice], target_joltage))
    return solns

def pick(choices, chain, target):
    if chain[-1] + 3 == target:
        return [chain + [target]]
    solns = []
    for choice in choices:
        if 1 <= choice - chain[-1] <= 3:
            solns.extend(pick(choices - set([choice]), chain + [choice], target))
    return solns

#print(pick(set(jolts), [0], max(jolts) + 3))
#print(pick(set(jolts), [14], 17))
#assert False

assert len(set(jolts)) == len(jolts) # no dupes.
jolts = sorted([0] + jolts)
must_pass_thru = []
for i in range(len(jolts)):
    if i > 0 and jolts[i] - jolts[i - 1] == 3:
        must_pass_thru.append(jolts[i])
must_pass_thru.append(max(jolts) + 3)
print(jolts)
print(len(must_pass_thru))
print(must_pass_thru)

print('-----')
current_jolts = 0
so_far = 1
for target_jolts in must_pass_thru:
    print('>>>>>')
    print(current_jolts)
    print(target_jolts)
    ways = pick(set(jolts), [current_jolts], target_jolts)
    print(ways)
    so_far *= len(ways)
    print(so_far)
    current_jolts = target_jolts
