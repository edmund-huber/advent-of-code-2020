#!/usr/bin/env python3
import sys

answer_lists = []
with open('input.txt') as f:
    answer_list = []
    for line in f:
        line = line.rstrip()
        if line == '':
            answer_lists.append(answer_list)
            answer_list = []
        else:
            answer_list.append(line)
    if answer_list != []:
        answer_lists.append(answer_list)

sum_ = 0
for l in answer_lists:
    yes_set = set()
    for answer in l:
        for a in answer:
            yes_set.add(a)
    sum_ += len(yes_set)
print(sum_)

sys.exit(1)
