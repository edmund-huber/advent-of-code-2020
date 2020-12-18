#!/usr/bin/env python3
import collections
import copy
import functools
import re

with open('input.txt') as f:
    for line in f:
        stack = []
        print('========')
        print(line)
        tokens = list(filter(lambda c: c not in ['', ' '], re.split(r'([( )])', line.strip())))
        print(tokens)
        for token in tokens:
            print(stack, token)
            if token == ' ':
                pass
            elif token == '(':
                pass
            elif token == ')':
                pass
            elif token in ['*', '+']:
                assert type(stack[-1]) is int
                stack.append(token)
            else:
                val2 = int(token)
                if len(stack) == 2:
                    op = stack.pop(-1)
                    val1 = stack.pop(-1)
                    assert type(val1) is int
                    if op == '+':
                        stack.append(val1 + val2)
                    elif op == '*':
                        stack.append(val1 * val2)
                    else:
                        assert False
                else:
                    stack.append(val2)
