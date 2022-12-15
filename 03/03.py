#!/usr/bin/env python3

import collections
import sys

def part1(lines):
    visits = collections.defaultdict(int)
    moves = { '^': (-1, 0), 'v': ( 1, 0), '>': ( 0,-1), '<': ( 0, 1) }
    loc = (0, 0)
    visits[loc] = 1
    for c in lines[0]:
        dr, dc = moves[c]
        loc = (loc[0] + dr, loc[1] + dc)
        visits[loc] += 1

    return len(visits)

def part2(lines):
    visits = collections.defaultdict(int)
    moves = { '^': (-1, 0), 'v': ( 1, 0), '>': ( 0,-1), '<': ( 0, 1) }
    loc1 = (0, 0)
    loc2 = (0, 0)
    visits[loc1] = 2
    for i in range(0, len(lines[0]), 2):
        dr1, dc1 = moves[lines[0][i]]
        dr2, dc2 = moves[lines[0][i+1]]
        loc1 = (loc1[0] + dr1, loc1[1] + dc1)
        loc2 = (loc2[0] + dr2, loc2[1] + dc2)
        visits[loc1] += 1
        visits[loc2] += 1

    return len(visits)

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
