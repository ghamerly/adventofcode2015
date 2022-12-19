#!/usr/bin/env python3

# https://adventofcode.com/2015/day/15 - "Science for Hungry People"
# Author: Greg Hamerly

import re
import sys

def solve(ingredients, count, ndx, constraint=None):
    if ndx + 1 == len(ingredients):
        count[-1] = 100 - sum(count[:-1])

        num_attributes = len(ingredients[0]) - 1 # ignore calories

        if constraint and not constraint(ingredients, count):
            return 0

        v = 1
        for a in range(num_attributes):
            v *= max(0, sum([i[a] * c for i, c in zip(ingredients, count)]))

        return v

    best = 0
    s = sum(count[:ndx])
    for c in range(100 - s):
        count[ndx] = c
        best = max(best, solve(ingredients, count, ndx + 1, constraint))

    return best

def part1(data):
    return solve(data, [0] * len(data), 0)

def part2(data):
    def calorie_constraint(ingredients, count):
        calories = sum(i[4] * c for i, c in zip(ingredients, count))
        return calories == 500

    return solve(data, [0] * len(data), 0, calorie_constraint)

def mogrify(line):
    parts = re.split('[^-0-9]+', line)
    return list(map(int, filter(None, parts)))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))

    print('part 1:', part1(data))
    print('part 2:', part2(data))

if __name__ == '__main__':
    main()
