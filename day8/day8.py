from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=8)

input = puzzle.input_data

trees = np.array(
    [[int(tree) for tree in line] for line in input.splitlines()]
)

width = len(trees)
height = len(trees[0])

visible = width * 2 + height * 2 - 4

for v_index in range(0, len(trees)):
    for h_index in range(0, len(trees[0])):
        if v_index != 0 and v_index != len(trees) - 1 and h_index != 0 and h_index != len(trees[0]) - 1:
            tallest_above = int(np.amax(trees[:v_index, h_index], initial=0))
            tallest_below = int(np.amax(trees[v_index + 1:, h_index], initial=0))
            tallest_to_left = int(np.amax(trees[v_index, :h_index], initial=0))
            tallest_to_right = int(np.amax(trees[v_index, h_index + 1:], initial=0))

            lowest_obstacle = min([tallest_above, tallest_below, tallest_to_left, tallest_to_right])

            visible += 1 if trees[v_index][h_index] > lowest_obstacle else 0