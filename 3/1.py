#!/usr/bin/env python3
import sys

m = []
with open('input.txt') as f:
    for line in f:
        m.append(line.rstrip())

x = 0
trees = 0
for line in m:
    if line[x] == '#':
        trees += 1
    x = (x + 3) % len(line)
print(trees)

sys.exit(1)
