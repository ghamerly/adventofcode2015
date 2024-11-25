#!/usr/bin/env python3

# https://adventofcode.com/2015/day/18 - "Like a GIF For Your Yard"
# Author: Greg Hamerly

import sys

def around(data, i, j):
    c = 0
    for ii in [i - 1, i, i + 1]:
        for jj in [j - 1, j, j + 1]:
            if 0 <= ii < len(data) and 0 <= jj < len(data[i]) and (ii != i or jj != j):
                c += (data[ii][jj] == '#')
    return c

def display(data):
    for row in data:
        print(''.join(row))

def part1(data):
    for iteration in range(100):
        next_state = [['.'] * len(row) for row in data]
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                num_on = around(data, i, j)
                if num_on == 3 or (col == '#' and num_on == 2):
                    next_state[i][j] = '#'
        data = next_state
    return sum([sum([c == '#' for c in row]) for row in data])

def part2(data):
    for iteration in range(100):
        next_state = [['.'] * len(row) for row in data]
        for i, row in enumerate(data):
            for j, col in enumerate(row):
                num_on = around(data, i, j)
                if num_on == 3 or (col == '#' and num_on == 2):
                    next_state[i][j] = '#'
        data = next_state

        # this is the difference - hold the corner lights "on"
        data[0][0] = data[0][-1] = data[-1][0] = data[-1][-1] = '#'

    return sum([sum([c == '#' for c in row]) for row in data])

def mogrify(line):
    return list(line)

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
