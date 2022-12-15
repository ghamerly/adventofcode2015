#!/usr/bin/env python3

# Simulate changing the brightness of lights in a grid of size 1000x1000.
# The meanings of the commands "turn on", "turn off", and "toggle" differ
# between part 1 and part 2.

import collections
import sys

def split(ab):
    return list(map(int, ab.split(',')))

def part1(lines):
    board = [[0] * 1000 for _ in range(1000)]
    for line in lines:
        tokens = line.split()

        if line.startswith('turn on'):
            a, b = map(split, (tokens[2], tokens[-1]))
            f = lambda r, c: 1
        elif line.startswith('turn off'):
            a, b = map(split, (tokens[2], tokens[-1]))
            f = lambda r, c: 0
        elif line.startswith('toggle'):
            a, b = map(split, (tokens[1], tokens[-1]))
            f = lambda r, c: 1 - board[r][c]
        else:
            assert False

        for r in range(a[0], b[0] + 1):
            for c in range(a[1], b[1] + 1):
                board[r][c] = f(r, c)
    
    return sum(map(sum, board))

def part2(lines):
    board = [[0] * 1000 for _ in range(1000)]
    for line in lines:
        tokens = line.split()

        if line.startswith('turn on'):
            a, b = map(split, (tokens[2], tokens[-1]))
            f = lambda r, c: board[r][c] + 1
        elif line.startswith('turn off'):
            a, b = map(split, (tokens[2], tokens[-1]))
            f = lambda r, c: max(0, board[r][c] - 1)
        elif line.startswith('toggle'):
            a, b = map(split, (tokens[1], tokens[-1]))
            f = lambda r, c: board[r][c] + 2
        else:
            assert False

        for r in range(a[0], b[0] + 1):
            for c in range(a[1], b[1] + 1):
                board[r][c] = f(r, c)
    
    return sum(map(sum, board))

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
