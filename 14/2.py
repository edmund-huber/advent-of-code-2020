#!/usr/bin/env python3
import collections
import copy

mem = {}

mask = None
with open('input.txt') as f:
    for line in f:
        dest, _, value = line.rstrip().split(' ')
        if dest == 'mask':
            mask = value
        else:
            value = int(value)
            _, addr, _ = dest.replace('[', ']').split(']')
            addr = int(addr)
            floats = []
            for i, b in enumerate(mask):
                if b == 'X':
                    floats.append(i)
                elif b == '1':
                    addr = addr | (1 << (35 - i))
                elif b == '0':
                    #addr = addr & ~(1 << (35 - i))
                    pass #fu
            if floats:
                combos = [addr]
                for i in floats:
                    new_combos = []
                    for c in combos:
                        new_combos.extend([
                            c | (1 << (35 - i)),
                            c & ~(1 << (35 - i))
                        ])
                    combos = new_combos
                for c in combos:
                    mem[c] = value
            else:
                mem[addr] = value
            assert mask is not None

print(sum(mem.values()))
