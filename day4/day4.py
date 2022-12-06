from aocd.models import Puzzle

import re

puzzle = Puzzle(year=2022, day=4)

input = puzzle.input_data

def in_range(first: range, second: range):
    return first.start >= second.start and first.stop <= second.stop

def overlapping(first: range, second: range):
    return range(max(first.start, second.start), min(first.stop, second.stop) + 1)

pairs = [(range(int(w), int(x)), range(int(y), int(z))) for w, x, y, z in re.findall('(\d+)-(\d+),(\d+)-(\d+)', input)]

answer1 = len([p for p in pairs if in_range(p[0], p[1]) or in_range(p[1], p[0])])
answer2 = len([p for p in pairs if overlapping(p[0], p[1])])

print(answer1)
print(answer2)