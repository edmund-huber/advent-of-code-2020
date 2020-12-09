#!/usr/bin/env python3

so_far = []
stream = []
with open('input.txt') as f:
    for line in f:
        n = int(line.rstrip())
        if len(stream) < 25:
            stream.append(n)
            so_far.append(n)
        else:
            ok = False
            for i, n1 in enumerate(stream):
                for j, n2 in enumerate(stream):
                    if i == j:
                        continue
                    if n1 + n2 == n:
                        ok = True
                        break
            print(stream)
            print(so_far)
            print(n)
            if not ok:
                for i, n1 in enumerate(so_far):
                    for j, n2 in enumerate(so_far):
                        if j < i + 2:
                            continue
                        if sum(so_far[i:j]) == n:
                            l = so_far[i:j]
                            print(min(l) + max(l))
                assert False
            stream = stream[1:] + [n]
            so_far.append(n)
