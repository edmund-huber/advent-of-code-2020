#!/usr/bin/env python3
import sys

values = []
valid = 0;
with open('input.txt') as f:
    for line in f:
        policy, password = line.split(': ')
        tokens = policy.split(' ')
        lo, hi = tokens[0].split('-')
        lo = int(lo)
        hi = int(hi)
        char = tokens[1]
        count = 0
        for c in password:
            if c == char:
                count += 1
        if count >= lo and count <= hi:
            valid += 1

print(valid)

sys.exit(1)

