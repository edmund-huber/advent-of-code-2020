#!/usr/bin/env python3
import sys

strings = []
with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        strings.append(line)

def bsp(s, min_, range_, lowchar, highchar):
    if len(s) == 0:
        assert range_ == 1
        return min_
    c = s[:1]
    new_range = range_ // 2
    if c == lowchar:
        print('LOW !  min=%i, range=%i' % (min_, new_range))
        return bsp(s[1:], min_, new_range, lowchar, highchar)
    elif c == highchar:
        new_min = min_ + (range_ // 2)
        print('LOW !  min=%i, range=%i' % (new_min, new_range))
        return bsp(s[1:], new_min, new_range, lowchar, highchar)
    else:
        assert False

def get_seat(s):
    row = bsp(s[:7], 0, 128, 'F', 'B')
    col = bsp(s[7:], 0, 8, 'L', 'R')
    return row, col

max_row = 0
max_col = 0
for string in strings:
    row, col = get_seat(string)
    max_row = max(max_row, row)
    max_col = max(max_col, col)

seats = set()
for row in range(max_row + 1):
    for col in range(max_col + 1):
        seats.add((row, col))
print(seats)

for string in strings:
    row, col = get_seat(string)
    seats.remove((row, col))

print(seats)

print((90 * 8) + 7)

#    seat_id = (row * 8) + col
#    highest_seat_id = max(highest_seat_id, seat_id)
#print(highest_seat_id)

sys.exit(1)
