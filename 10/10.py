#!/usr/bin/env python3

# https://adventofcode.com/2015/day/10 - "Elves Look, Elves Say"
# Author: Greg Hamerly

# There is very likely a more efficient way to calculate this. But, brute force
# works in 5 seconds, so we'll just do that.

import sys

def look_and_say(l):
    '''Turn '11133' into '3123', etc. according to the rules of 'look and say'.'''
    seq = [[0, l[0]]]
    for c in l:
        if c == seq[-1][1]:
            seq[-1][0] += 1
        else:
            seq.append([1, c])
    return ''.join([str(count) + char for count, char in seq])

def part1(line):
    for i in range(40):
        line = look_and_say(line)
    return len(line)

def part2(line):
    for i in range(50):
        line = look_and_say(line)
    return len(line)

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    print('part 1:', part1(lines[0]))
    print('part 2:', part2(lines[0]))

if __name__ == '__main__':
    main()
