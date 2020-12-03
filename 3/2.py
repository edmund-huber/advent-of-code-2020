#!/usr/bin/env python3
import sys

m = []
with open('input.txt') as f:
    for line in f:
        m.append(line.rstrip())

def tree_count(d_x, d_y):
    x = 0
    y = 0
    trees = 0
    while y < len(m):
        line = m[y]
        if line[x] == '#':
            trees += 1
        y += d_y
        x = (x + d_x) % len(line)
    return trees

print(tree_count(1, 1) * tree_count(3, 1) * tree_count(5, 1) * tree_count(7, 1) * tree_count(1, 2))

sys.exit(1)
