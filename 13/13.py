#!/usr/bin/env python3

# https://adventofcode.com/2015/day/13 - "Knights of the Dinner Table"
# Author: Greg Hamerly

import itertools
import sys

def part1(graph):
    '''The data set is small enough (n <= 8) that O(n!) is fast enough.'''
    n = len(graph)
    ans = -1e100
    for o in itertools.permutations(graph):
        happiness = 0
        for i in range(len(o)):
            a, b = o[i], o[(i + 1) % n]
            happiness += graph[a][b] + graph[b][a]
        ans = max(ans, happiness)
    return ans

def part2(graph):
    me = 'Me'
    graph[me] = {person: 0 for person in graph}
    for person in graph:
        graph[person][me] = 0
    return part1(graph)

def mogrify(line):
    parts = line.strip('.').split()
    source, sign, units, neighbor = [parts[i] for i in [0, 2, 3, -1]]
    units = (-1 if sign == 'lose' else 1) * int(units)
    return source, units, neighbor

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))

    graph = {src: {} for src, _, _, in data}
    for src, cost, dest in data:
        graph[src][dest] = cost

    print('part 1:', part1(graph))
    print('part 2:', part2(graph))

if __name__ == '__main__':
    main()
