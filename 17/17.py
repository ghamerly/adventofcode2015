#!/usr/bin/env python3

# https://adventofcode.com/2015/day/17 - "No Such Thing as Too Much"
# Author: Greg Hamerly

# this is the number of ways to sum to 150, which can be solved via dynamic
# programming
#   - 1 way to make a sum of 0

import sys
import itertools

def part1(data):
    # find out how many different ways we can make a sum of 150 using the
    # numbers given in the input. There's one way to make a sum of 0, and we
    # keep adding in new options with every number.
    table = [[0] * 151 for _ in range(len(data) + 1)]
    table[0][0] = 1 # one way to make a sum of 0
    for i, container in enumerate(data):
        for j in range(151):
            # if we could previously make this sum, we can make it again
            # (without using the i'th container)
            table[i+1][j] += table[i][j]

            # also, if there are other ways of making the sum *with* this
            # container, use this container
            if j - container >= 0 and table[i][j - container]:
                table[i+1][j] += table[i][j - container]

    return table[-1][-1]

def part2(data):
    for num_bins in range(len(data) + 1):
        num_ways = 0
        for bins in itertools.combinations(data, num_bins):
            if sum(bins) == 150:
                num_ways += 1

        if num_ways:
            return num_ways

def mogrify(line):
    return int(line)

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
