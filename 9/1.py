#!/usr/bin/env python3

stream = []
with open('input.txt') as f:
    for line in f:
        n = int(line.rstrip())
        if len(stream) < 25:
            stream.append(n)
        else:
            ok = False
            for i, n1 in enumerate(stream):
                for j, n2 in enumerate(stream):
                    if i == j:
                        continue
                    if n1 + n2 == n:
                        ok = True
                        break
            assert ok, n
            stream = stream[1:] + [n]
