#!/usr/bin/env python3
import collections
import copy

mask = None
mem = []
with open('input.txt') as f:
    for line in f:
        dest, _, value = line.rstrip().split(' ')
        if dest == 'mask':
            mask = value
        else:
            value = int(value)
            _, addr, _ = dest.replace('[', ']').split(']')
            addr = int(addr)
            if addr >= len(mem):
                extra = addr - len(mem) + 1
                mem.extend([0] * extra)
            for i, b in enumerate(mask):
                if b == 'X':
                    pass
                elif b == '1':
                    value = value | (1 << (35 - i))
                elif b == '0':
                    value = value & ~(1 << (35 - i))
            mem[addr] = value
            assert mask is not None

print(sum(mem))
