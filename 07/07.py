#!/usr/bin/env python3

import re
import sys

def simulate(commands):
    '''Simulate via a fairly brute-force BFS.'''
    state = {}
    frontier = [(f, dest) for dest, (r, f) in commands.items() if r(state)]
    MASK = (1 << 16) - 1
    while frontier:
        new_frontier = []
        for f, dest in frontier:
            state[dest] = f(state) & MASK

            # This I don't like... examining all the commands every time
            for dest, (r, f) in commands.items():
                if dest not in state and r(state):
                    new_frontier.append((f, dest))
                    state[dest] = None # so we don't do it again this round

        frontier = new_frontier

    return state.get('a')

def part1(commands):
    return simulate(commands)

def part2(commands):
    a_value = simulate(commands)
    commands['b'] = (lambda state: True, lambda state: a_value) # from part 1
    return simulate(commands)

def mogrify(line):
    src, dest = line.split(' -> ')
    f = None
    if re.match('^[0-9]+$', src):
        r = lambda state: True
        f = lambda state: int(src)
    elif re.match('^[a-z]+$', src):
        r = lambda state: src in state
        f = lambda state: state[src]
    elif re.match('^[a-z]+ RSHIFT [0-9]+$', src):
        reg, op, dist = src.split()
        r = lambda state: reg in state
        f = lambda state: state[reg] >> int(dist)
    elif re.match('^[a-z]+ LSHIFT [0-9]+$', src):
        reg, op, dist = src.split()
        r = lambda state: reg in state
        f = lambda state: state[reg] << int(dist)
    elif re.match('^[a-z]+ AND [a-z]+$', src):
        reg1, op, reg2 = src.split()
        r = lambda state: reg1 in state and reg2 in state
        f = lambda state: state[reg1] & state[reg2]
    elif re.match('^[0-9]+ AND [a-z]+$', src):
        const, op, reg = src.split()
        r = lambda state: reg in state
        f = lambda state: int(const) & state[reg]
    elif re.match('^[a-z]+ OR [a-z]+$', src):
        reg1, op, reg2 = src.split()
        r = lambda state: reg1 in state and reg2 in state
        f = lambda state: state[reg1] | state[reg2]
    elif re.match('^NOT [a-z]+$', src):
        op, reg = src.split()
        r = lambda state: reg in state
        f = lambda state: ~state[reg]
    else:
        assert False, line

    return (dest, (r, f))

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = list(map(str.strip, f))

    commands = dict(map(mogrify, lines))

    print('part 1:', part1(commands))
    print('part 2:', part2(commands))

if __name__ == '__main__':
    main()
