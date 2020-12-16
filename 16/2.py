#!/usr/bin/env python3
import collections
import copy
import functools

with open('input.txt') as f:
    # rules
    rules = collections.defaultdict(list)
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        field, to_parse = line.split(': ')
        for range_ in to_parse.split(' or '):
            lo, hi = range_.split('-')
            rules[field].append((int(lo), int(hi)))

    tickets = []
    assert f.readline() == 'your ticket:\n'
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        tickets.append(list(map(int, line.split(','))))

    assert f.readline() == 'nearby tickets:\n'
    for line in f:
        line = line.rstrip()
        if line == '':
            break
        tickets.append(list(map(int, line.split(','))))

new_tickets = []
for ticket in tickets:
    discarding = False
    for value in ticket:
        have_a_rule = False
        for field, rule in rules.items():
            for lo, hi in rule:
                have_a_rule |= value >= lo and value <= hi
        if not have_a_rule:
            discarding = True
    if not discarding:
        new_tickets.append(ticket)
print(len(tickets))
print(len(new_tickets))
tickets = new_tickets

cols = list(range(len(tickets[0])))
known_cols = {}
known_fields = set()
while len(known_cols) < len(cols):
    field_must_bes = []
    for col in cols:
        if col in known_cols:
            continue
        valid_fields_per_value = []
        for value in map(lambda t: t[col], tickets):
            valid_fields = set()
            for field, lohis in rules.items():
                field_is_valid = False
                for lo, hi in lohis:
                    field_is_valid |= value >= lo and value <= hi
                if field_is_valid:
                    valid_fields.add(field)
            valid_fields -= known_fields
            valid_fields_per_value.append(valid_fields)
        intersection = functools.reduce(lambda so_far, s: so_far & s, valid_fields_per_value)
        if len(intersection) == 1:
            field_must_bes.append((col, list(intersection)[0]))

    assert len(field_must_bes) > 0
    assert len(set(field_must_bes)) == len(field_must_bes)
    for col, must_be_field in field_must_bes:
        assert col not in known_cols
        known_cols[col] = must_be_field
        known_fields.add(must_be_field)

print(known_cols)

# assuming my ticket was valid heh:
acc = 1
for col, value in enumerate(tickets[0]):
    if known_cols[col].startswith('departure'):
        acc *= value
print(acc)
