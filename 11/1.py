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
            return [row[i]]
    return []

def pprint():
    for row in seats:
        print(''.join(row))

while True:
    print('----')
    pprint()
    new_seats = copy.deepcopy(seats)
    for j, row in enumerate(seats):
        for i, s in enumerate(row):
            neighbors = get(i-1, j+1) + get(i, j+1) + get(i+1, j+1) + get(i-1, j) + get(i+1, j) + get(i-1, j-1) + get(i, j-1) + get(i+1, j-1)
            if s == 'L' and all(n in ['L', '.'] for n in neighbors):
                new_seats[j][i] = '#'
            elif s == '#' and len(list(filter(lambda n: n == '#', neighbors))) >= 4:
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
