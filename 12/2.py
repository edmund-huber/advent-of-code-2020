#!/usr/bin/env python3
import collections
import copy

x = 10
y = 1
def spin(deg):
    global x
    global y
    assert deg % 90 == 0
    while deg != 0:
        if deg > 0:
            deg -= 90
            x, y = y, -x
        elif deg < 0:
            deg += 90
            x, y = -y, x
        else:
            assert False

ship_x = 0
ship_y = 0
with open('input.txt') as f:
    for line in f:
        cmd = line.rstrip()
        op = cmd[0]
        count = int(cmd[1:])
        if op == 'N':
            y += count
        elif op == 'S':
            y -= count
        elif op == 'E':
            x += count
        elif op == 'W':
            x -= count
        elif op == 'L':
            spin(-count)
        elif op == 'R':
            spin(count)
        elif op == 'F':
            ship_x += x * count
            ship_y += y * count
        else:
            assert False
        print("ship: {}, {}  way: {}, {}".format(ship_x, ship_y, x, y))

print(abs(ship_x) + abs(ship_y))
