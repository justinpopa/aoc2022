from aocd.models import Puzzle

import re

puzzle = Puzzle(year=2022, day=5)

input = puzzle.input_data

column_line = re.search('^(?:\W+\d+\W)+$', input, re.MULTILINE)

columns = [index for index, char in enumerate(input[column_line.start():column_line.end()]) if char.isdigit()]

raw_stacks, moves = re.split('^(?:\W+\d+\W)+\n\n', input, flags=re.MULTILINE)

def set_columns(raw_stacks, columns):
    tmp_stack = [[] for i in range(len(columns))]

    for stack in raw_stacks.splitlines():
        for c in range(len(stack)):
            if c in columns and stack[c].isalpha():
                tmp_stack[columns.index(c)].append(stack[c])

    return tmp_stack

def move_crates(amount, source, dest, stacks):
    crates = stacks[source - 1][0:amount]
    stacks[dest - 1] = crates + stacks[dest - 1]
    [stacks[source -1].remove(c) for c in crates]

answer1 = set_columns(raw_stacks, columns)
answer2 = set_columns(raw_stacks, columns)

for move in moves.splitlines():
    amount, source, dest = re.findall('(\d+) from (\d+) to (\d+)', move).pop()

    for x in range(int(amount)):
        move_crates(1, int(source), int(dest), answer1)

    move_crates(int(amount), int(source), int(dest), answer2)

print(''.join([i[0] for i in answer1]))
print(''.join([i[0] for i in answer2]))