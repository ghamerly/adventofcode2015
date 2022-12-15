#!/usr/bin/env python3

import hashlib
import sys

def part1(lines):
    h = hashlib.md5()
    h.update(lines[0].encode('utf-8'))
    q = ['']
    while q:
        for suffix in q:
            h2 = h.copy()
            h2.update(suffix.encode('utf-8'))
            if h2.hexdigest()[:5] == '00000':
                return suffix
            for c in '123456789':
                q.append(suffix + c)

def dldfs(h, suffix, depth):
    if depth == 0:
        return h.hexdigest()[:6] == '000000'

    suffix.append('')
    for i in '123456789':
        suffix[-1] = i
        h2 = h.copy()
        h2.update(i.encode('utf-8'))
        if dldfs(h2, suffix, depth - 1):
            return True
    suffix.pop()

def part2_dfs(lines):
    depth = 0
    while True:
        h = hashlib.md5()
        h.update(lines[0].encode('utf-8'))
        suffix = []
        if dldfs(h, suffix, depth):
            return ''.join(suffix)
        depth += 1

def part2_bfs(lines):
    h = hashlib.md5()
    h.update(lines[0].encode('utf-8'))
    q = ['']
    while q:
        for suffix in q:
            h2 = h.copy()
            h2.update(suffix.encode('utf-8'))
            if h2.hexdigest()[:6] == '000000':
                return suffix
            for c in '123456789':
                q.append(suffix + c)

part2 = part2_dfs

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
