#!/usr/bin/env python3

import collections
import sys

# Rules about what makes a "nice string" for part 1:
# - It contains at least three vowels (aeiou only), like aei, xazegov, or
#   aeiouaeiouaeiou.
# - It contains at least one letter that appears twice in a row, like xx, abcdde
#   (dd), or aabbccdd (aa, bb, cc, or dd).
# - It does not contain the strings ab, cd, pq, or xy, even if they are part of
#   one of the other requirements.

def nice1(line):
    three_vowels = sum([line.count(c) for c in 'aeiou']) >= 3
    double = False
    for i in range(1, len(line)):
        if line[i] == line[i-1]:
            double = True
            break
    bad = any(b in line for b in ['ab', 'cd', 'pq', 'xy'])

    return three_vowels and double and not bad

def part1(lines):
    return sum(map(nice1, lines))

# Rules for part 2:
# - It contains a pair of any two letters that appears at least twice in the
# string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
# aaa (aa, but it overlaps).
# - It contains at least one letter which repeats with exactly one letter
# between them, like xyx, abcdefeghi (efe), or even aaa.

def nice2(line):
    pairs = [line[i-1:i+1] for i in range(1, len(line))]

    pairs_indexes = collections.defaultdict(list)
    for i, p in enumerate(pairs):
        pairs_indexes[p].append(i)

    has_disjoint_pair = any(max(idx) - min(idx) > 1 for idx in pairs_indexes.values())

    has_two_peat = any(line[i-2] == line[i] for i in range(2, len(line)))

    return has_disjoint_pair and has_two_peat

def part2(lines):
    return sum(map(nice2, lines))

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
