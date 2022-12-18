#!/usr/bin/env python3

# https://adventofcode.com/2015/day/12 - "JSAbacusFramework.io"
# Author: Greg Hamerly

import json
import re
import sys

def part1(lines):
    p = re.compile('-?[0-9]+')
    return [sum([int(m.group()) for m in p.finditer(line)]) for line in lines]

def try_int(x):
    try:
        return int(x)
    except:
        return 0

def sum_non_red(obj):
    if isinstance(obj, dict):
        ans = 0
        for k, v in obj.items():
            if v == "red":
                return 0
            ans += try_int(k) + sum_non_red(v)
        return ans
    elif isinstance(obj, list):
        return sum(map(sum_non_red, obj))
    else:
        return try_int(obj)

def part2(lines):
    return [sum_non_red(json.loads(line)) for line in lines]

def main():
    regular_input = __file__.split('/')[-1][:-len('.py')] + '.in'
    file = regular_input if len(sys.argv) <= 1 else sys.argv[1]
    print(f'using input: {file}')
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]

    print('part 1:', part1(lines))
    print('part 2:', part2(lines))

if __name__ == '__main__':
    main()
