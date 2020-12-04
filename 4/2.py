#!/usr/bin/env python3
import sys

passports = []
current = {}
with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        if line == '':
            passports.append(current)
            current = {}
            continue
        for token in line.split(' '):
            key, value = token.split(':')
            current[key] = value
    if current != {}:
        passports.append(current)

def valid(passport):
    if not set(passport.keys()).issuperset('byr iyr eyr hgt hcl ecl pid'.split()):
        print('(keys)')
        return False
    if not (len(passport['byr']) == 4 and (1920 <= int(passport['byr']) <= 2002)):
        print('byr')
        return False
    if not (len(passport['iyr']) == 4 and (2010 <= int(passport['iyr']) <= 2020)):
        print('iyr')
        return False
    if not (len(passport['eyr']) == 4 and (2020 <= int(passport['eyr']) <= 2030)):
        print('eyr')
        return False
    hgt = passport['hgt']
    hgt_cm = hgt.endswith('cm')
    hgt_in = hgt.endswith('in')
    if hgt_cm or hgt_in:
        hgt = hgt[:-2]
        if hgt_cm and (150 <= int(hgt) <= 193):
            pass
        elif hgt_in and (59 <= int(hgt) <= 76):
            pass
        else:
            print('hgt: ' + hgt)
            return False
    else:
        print('hgt')
        return False
    hcl = passport['hcl']
    if not (len(hcl) == 7 and hcl[0] == '#' and (c in '0123456789abcdef' for c in hcl[1:])):
        print('hcl')
        return False
    ecl = passport['ecl']
    if not (ecl in 'amb blu brn gry grn hzl oth'.split()):
        print('ecl')
        return False
    pid = passport['pid']
    try:
        int(pid) # check is number lol
        if not (len(pid) == 9):
            print('pid')
            return False
    except:
        print('pid')
        return False
    return True

no_valid = 0
for passport in passports:
    if valid(passport):
        no_valid += 1
    else:
        print(passport)
print(no_valid)

sys.exit(1)
