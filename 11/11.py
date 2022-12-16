#!/usr/bin/env python3

# https://adventofcode.com/2015/day/11 - "Corporate Policy"
# Author: Greg Hamerly

import sys

BAD_i = ord('i') - ord('a')
BAD_o = ord('o') - ord('a')
BAD_l = ord('l') - ord('a')

def valid(p):
    '''Implement the rules of the problem. Note that the values are in reverse
    order, so an increasing sequence in the original order becomes a decreasing
    sequence here.'''

    # should have an increasing 3-letter sequence (which here is decreasing
    # since the number is in reverse order)
    for i in range(2, len(p)):
        if p[i-2] - 2 == p[i-1] - 1 == p[i]:
            break
    else:
        return False

    # should not have any bad characters
    if BAD_i in p or BAD_o in p or BAD_l in p:
        return False

    # must have two double character sequences
    i = 1
    doubles = 0
    while i < len(p):
        if p[i-1] == p[i]:
            doubles += 1
            i += 1
        i += 1

    return doubles >= 2

def increment(p):
    '''Add one in base-26; operates in place.'''
    for i in range(len(p)):
        # determine if there is a carry or not
        if p[i] == 25:
            p[i] = 0
        else:
            p[i] += 1
            break
    else:
        # if we get all the way to the end, we had a carryout
        p.append(1)

def part1(p):
    while True:
        increment(p)
        if valid(p):
            a = ord('a')
            return ''.join([chr(c + a) for c in p[::-1]])

def part2(p):
    return part1(mogrify(part1(p)))

def mogrify(line):
    # reverse the order so that we can work with little-endian numbers, and
    # convert to integers in base-26 by subtracting off 'a'
    return [ord(c) - ord('a') for c in line[::-1]]

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))

    print('part 1:', part1(list(data[0])))
    print('part 2:', part2(list(data[0])))

if __name__ == '__main__':
    main()
