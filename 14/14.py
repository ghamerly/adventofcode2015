#!/usr/bin/env python3

# https://adventofcode.com/2015/day/14 - "Reindeer Olympics"
# Author: Greg Hamerly

import sys

class Reindeer:
    def __init__(self, speed, duration, rest):
        self.speed    = speed
        self.duration = duration
        self.rest     = rest

    def traveled(self, time):
        cycle_time = self.duration + self.rest
        remainder = time % cycle_time
        cycles = time // cycle_time
        return self.speed * (cycles * self.duration + min(self.duration, remainder))

def part1(reindeer):
    return max([r.traveled(2503) for r in reindeer])

def part2(reindeer):
    points = [0] * len(reindeer)

    for i in range(1, 2504):
        traveled = [(r.traveled(i), j) for j, r in enumerate(reindeer)]
        furthest = max(traveled)[0]
        for dist, j in traveled:
            if dist == furthest:
                points[j] += 1

    return max(points)

def mogrify(line):
    parts = line.split()
    return Reindeer(int(parts[3]), int(parts[6]), int(parts[13]))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    reindeer = list(map(mogrify, lines))

    print('part 1:', part1(reindeer))
    print('part 2:', part2(reindeer))

if __name__ == '__main__':
    main()
