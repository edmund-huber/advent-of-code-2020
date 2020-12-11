#!/usr/bin/env python3
import collections
import copy

seats = []
with open('input.txt') as f:
    for line in f:
        seats.append(list(line.rstrip()))
print(seats)

def get(i, j):
    if 0 <= j < len(seats):
        row = seats[j]
        if 0 <= i < len(row):
            return [(i, j, row[i])]
    return []

def get_cast(i, j, s_x, s_y):
    while True:
        i += s_x
        j += s_y
        if not (0 <= j < len(seats)):
            return []
        row = seats[j]
        if not (0 <= i < len(row)):
            return []
        if row[i] != '.':
            return [(i, j, row[i])]

def pprint():
    for row in seats:
        print(''.join(row))

def combine(res):
    seen_coords = set()
    new_res = []
    for i, j, s in res:
        if (i, j) not in seen_coords:
            new_res.append(s)
            seen_coords.add((i, j))
    return new_res

while True:
    print('----')
    pprint()
    new_seats = copy.deepcopy(seats)
    for j, row in enumerate(seats):
        for i, s in enumerate(row):
            neighbors = get(i-1, j+1) + get(i, j+1) + get(i+1, j+1) + get(i-1, j) + get(i+1, j) + get(i-1, j-1) + get(i, j-1) + get(i+1, j-1) + \
                get_cast(i, j, 0, 1) + \
                get_cast(i, j, 1, 1) + \
                get_cast(i, j, 1, 0) + \
                get_cast(i, j, 1, -1) + \
                get_cast(i, j, 0, -1) + \
                get_cast(i, j, -1, -1) + \
                get_cast(i, j, -1, 0) + \
                get_cast(i, j, -1, 1)
            #print(neighbors)
            #print(combine(neighbors))
            #break
            neighbors = combine(neighbors)
            if s == 'L' and all(n in ['L', '.'] for n in neighbors):
                new_seats[j][i] = '#'
            elif s == '#' and len(list(filter(lambda n: n == '#', neighbors))) >= 5:
                new_seats[j][i] = 'L'
    if new_seats == seats:
        break
    seats = new_seats

occupied = 0
for j, row in enumerate(seats):
    for i, s in enumerate(row):
        if seats[j][i] == '#':
            occupied += 1
print(occupied)
