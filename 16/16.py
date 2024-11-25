#!/usr/bin/env python3

# https://adventofcode.com/2015/day/16 - "Aunt Sue"
# Author: Greg Hamerly

import re
import sys

known_data = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
        }

def equal(x): return lambda y: x == y
def less_than(x): return lambda y: x < y
def greater_than(x): return lambda y: x > y

def solve(data, data_filter):
    for num, desc in data:
        for k in desc:
            assert k in data_filter
            if not data_filter[k](desc[k]):
                break
        else:
            return num

def mogrify(line):
    parts = re.split('[ :,]+', line)
    num = parts[1]
    d = {}
    for i in range(2, len(parts), 2):
        d[parts[i]] = int(parts[i+1])
    return num, d

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))

    part1_filter = {k: equal(v) for k, v in known_data.items()}
    part2_filter = {}
    for k, v in known_data.items():
        if k in ('cats', 'trees'):
            part2_filter[k] = less_than(v)
        elif k in ('pomeranians', 'goldfish'):
            part2_filter[k] = greater_than(v)
        else:
            part2_filter[k] = equal(v)

    print('part 1:', solve(data, part1_filter))
    print('part 2:', solve(data, part2_filter))

if __name__ == '__main__':
    main()
