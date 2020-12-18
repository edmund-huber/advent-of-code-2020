#!/usr/bin/env python3
import collections
import copy
import functools
import re

sum_ = 0
with open('input.txt') as f:
    for line in f:
        stacks = [[]]
        print('========')
        print(line)
        tokens = list(filter(lambda c: c not in ['', ' '], re.split(r'([( )])', line.strip())))
        new_tokens = ['((']
        for token in tokens:
            if token == '+':
                new_tokens.append(')+(')
            elif token == '*':
                new_tokens.append('))*((')
            elif token == '(':
                new_tokens.append('(((')
            elif token == ')':
                new_tokens.append(')))')
            else:
                new_tokens.append(token)
        new_tokens.append('))')
        print(tokens)
        print(new_tokens)
        sum_ += eval(''.join(new_tokens))
print(sum_)
