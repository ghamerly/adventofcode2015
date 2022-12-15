#!/usr/bin/env python3

import sys

def part1(dims):
    return sum(2 * (a * b + a * c + b * c) + (a * b) for a, b, c in dims)

def part2(dims):
    return sum(a * b * c + 2 * a + 2 * b for a, b, c in dims)

def parse(lines):
    return [sorted(map(int, line.split('x'))) for line in lines]

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    dims = parse(lines)

    print('part 1:', part1(dims))
    print('part 2:', part2(dims))

if __name__ == '__main__':
    main()
