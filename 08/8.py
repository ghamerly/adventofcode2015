#!/usr/bin/env python3

# https://adventofcode.com/2015/day/8 - "Matchsticks"
# Author: Greg Hamerly

import sys

def part1(lines):
    # cheat by using eval to un-escape the string and remove the enclosing
    # quotes
    return sum([len(line) - len(eval(line)) for line in lines])

def part2(lines):
    # each escaped character is doubled, and we add 2 enclosing quotes
    # so the difference between the original and new line is the number of
    # characters we need to escape (one backslash for each) plus 2
    return sum([line.count('"') + line.count('\\') + 2 for line in lines])

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
