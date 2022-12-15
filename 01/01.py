#!/usr/bin/env python3

import sys

def part1(lines):
    m = {'(': 1, ')': -1}
    return sum(map(m.__getitem__, lines[0]))

def part2(lines):
    m = {'(': 1, ')': -1}
    s = 0
    for i, c in enumerate(lines[0]):
        s += m[c]
        if s == -1:
            return i + 1

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
