#!/usr/bin/env python3
import sys

rules = []
with open('input.txt') as f:
    for line in f:
        line = line.rstrip()
        bag1, bags = line.split(' contain ')
        bag1 = bag1.rstrip('s')
        rhs = []
        if bags != 'no other bags.':
            for bag in bags.split(', '):
                bag = bag.rstrip('.')
                quantity = int(bag.split(' ')[0])
                bag = ' '.join(bag.split(' ')[1:]).rstrip('s')
                rhs.append((quantity, bag))
        rules.append((bag1, rhs))

def find_lhs_by_rhs(bag):
    results = set()
    for lhs_bag, rhs_bags in rules:
        for quantity, rhs_bag in rhs_bags:
            if rhs_bag == bag:
                results.add(lhs_bag)
                continue
    return results

print(rules[0])
print(find_lhs_by_rhs('shiny gold bag'))

found_bags = set(['shiny gold bag'])
while True:
    print(found_bags)
    new_found_bags = set()
    for found_bag in found_bags:
        for new_found_bag in find_lhs_by_rhs(found_bag):
            new_found_bags.add(new_found_bag)
    if len(new_found_bags - found_bags) == 0:
        break
    found_bags.update(new_found_bags)
print(len(found_bags - set(['shiny gold bag'])))

just_the_color = set()
for found_bag in found_bags:
    type_, color, _ = found_bag.split(' ')
    just_the_color.add(color)
print(len(just_the_color - set(['gold'])))

def count(start_bag):
    count_ = 1
    for lhs_bag, rhs_bags in rules:
        if lhs_bag == start_bag:
            for quantity, rhs_bag in rhs_bags:
                count_ += quantity * count(rhs_bag)
                assert quantity != 0
            break
    return count_

print(count('shiny gold bag') - 1)

sys.exit(1)
