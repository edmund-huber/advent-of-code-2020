#!/usr/bin/env python3
import sys

values = []
with open('input.txt') as f:
    for line in f:
        values.append(int(line))

for v1 in values:
    for v2 in values:
        for v3 in values:
            if v1 + v2 + v3 == 2020:
                print(v1 * v2 * v3)
                sys.exit(0)
sys.exit(1)
