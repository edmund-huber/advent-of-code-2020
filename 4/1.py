#!/usr/bin/env python3
import sys

passports = []
current = {}
with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            print(current)
            passports.append(current)
            current = {}
            continue
        for token in line.split(' '):
            key, value = token.split(':')
            current[key] = value
    if current != {}:
        passports.append(current)

def valid(passport):
    print(set(passport.keys()))
    if set(passport.keys()) == set('byr iyr eyr hgt hcl ecl pid'.split()):
        print('yes')
        return True
    elif set(passport.keys()) == set('byr iyr eyr hgt hcl ecl pid'.split()):
        print('yup')
        return True
    print('no')
    return False

no_valid = 0
for passport in passports:
    if valid(passport):
        no_valid += 1
print(no_valid)

sys.exit(1)
