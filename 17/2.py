#!/usr/bin/env python3
import collections
import copy
import functools

# wzyx
state_ctr = lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(bool))))
state = state_ctr()

def print_state(): # not gonna fix this for w
    print('%%%%%%%%%%%%%%%%%%')
    min_z = min(state.keys())
    max_z = max(state.keys())
    for z in range(min_z, max_z + 1):
        print('z =', z)
        min_y = min(state[z].keys())
        max_y = max(state[z].keys())
        for y in range(min_y, max_y + 1):
            min_x = min(state[z][y].keys())
            max_x = max(state[z][y].keys())
            for x in range(min_x, max_x + 1):
                print('#' if state[z][y][x] else '.', end='')
            print()
        print()

def neighbors(w, z, y, x):
    n = set()
    for w_off in [-1, 0, 1]:
        for z_off in [-1, 0, 1]:
            for y_off in [-1, 0, 1]:
                for x_off in [-1, 0, 1]:
                    n.add((w + w_off, z + z_off, y + y_off, x + x_off))
    n.remove((w, z, y, x))
    assert len(n) == 80
    return n

with open('input.txt') as f:
    y = 0
    for line in f:
        for x, c in enumerate(line.rstrip()):
            state[0][0][y][x] = c == '#'
        y += 1

for _ in range(6):
    #print_state()

    # find coords of all active cubes
    active_cubes = set()
    for w in state.keys():
        for z in state[w].keys():
            for y in state[w][z].keys():
                for x in state[w][z][y].keys():
                    active_cubes.add((w, z, y, x)) # this is slightly wrong but it doesnt matter

    # find set of all neighbors of all active cubes, this is the set to consider for the rules
    to_consider = set()
    for w, z, y, x in active_cubes:
        for wzyx in neighbors(w, z, y, x):
            to_consider.add(wzyx)

    # apply the rules
    new_state = state_ctr()
    for w, z, y, x in to_consider:
        n = len(list(filter(None, map(lambda wzyx: state[wzyx[0]][wzyx[1]][wzyx[2]][wzyx[3]], neighbors(w, z, y, x)))))
        if state[w][z][y][x]:
            new_state[w][z][y][x] = n in [2, 3]
        else:
            new_state[w][z][y][x] = n == 3
    state = new_state

#print_state()

count = 0
for w in state.keys():
    for z in state[w].keys():
        for y in state[w][z].keys():
            for x in state[w][z][y].keys():
                if state[w][z][y][x]:
                    count += 1
print(count)
