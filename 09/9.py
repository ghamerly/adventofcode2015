#!/usr/bin/env python3

# https://adventofcode.com/2015/day/9 - "All in a Single Night"
# Author: Greg Hamerly

import sys

def all_permutations_rec(graph, order, cost, best_cost, operator):
    '''Try all permutations. No pruning or clever data structures, since the
    input is very small.'''
    if len(order) == len(graph):
        best_cost[0] = operator(cost, best_cost[0])
        return

    current = order[-1]
    for u, c in graph[current].items():
        if u not in order:
            order.append(u)
            all_permutations_rec(graph, order, cost + c, best_cost, operator)
            order.pop()

def all_permutations(graph, init, operator):
    best_cost = [init]
    for u in graph:
        order = [u]
        cost = 0
        all_permutations_rec(graph, order, cost, best_cost, operator)
    return best_cost[0]

def part1(graph):
    return all_permutations(graph, 1e100, min)

def part2(graph):
    return all_permutations(graph, -1, max)

def mogrify(line):
    parts = line.split()
    return parts[0], parts[2], int(parts[-1])

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    data = list(map(mogrify, lines))
    graph = {u: {} for u,_,_ in data} | {v: {} for _,v,_ in data}
    for u, v, l in data:
        graph[u][v] = l
        graph[v][u] = l

    print('part 1:', part1(graph))
    print('part 2:', part2(graph))

if __name__ == '__main__':
    main()
