from aocd.models import Puzzle

import re

puzzle = Puzzle(year=2022, day=5)

input = puzzle.input_data

column_line = re.search('^(?:\W+\d+\W)+$', input, re.MULTILINE)

columns = [index for index, char in enumerate(input[column_line.start():column_line.end()]) if char.isdigit()]

raw_stacks, moves = re.split('^(?:\W+\d+\W)+\n', input, flags=re.MULTILINE)

stacks = []

for column in columns:
    tmp_stack = []
    for stack in raw_stacks.splitlines():

        for c in range(0, len(stack), 1):
            if c == column and stack[c].isalpha():
                tmp_stack.append(stack[c])
    stacks.append(tmp_stack)

