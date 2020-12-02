#!/usr/bin/env python3
import sys

valid_count = 0
with open('input.txt') as f:
    for line in f:
        policy, password = line.split(': ')
        tokens = policy.split(' ')
        lo, hi = tokens[0].split('-')
        pos1 = int(lo)
        pos2 = int(hi)
        char = tokens[1]
        valid = 0
        for i, c in enumerate(password):
            if i + 1 in [pos1, pos2] and c == char:
                valid += 1
        if valid == 1:
            valid_count += 1

print(valid_count)

sys.exit(1)
