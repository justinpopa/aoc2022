from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=8)

input = puzzle.input_data
input2 = """30373
25512
65332
33549
35390"""

trees = np.array(
    [[int(tree) for tree in line] for line in input.splitlines()]
)

visible = len(trees) * 2 + len(trees[0]) * 2 - 4
most_scenic = 0

def get_score(trees, tree):
    score = 0
    for t in trees:
        score += 1
        if t >= tree:
            break
    return score

for v_index in range(0, len(trees)):
    for h_index in range(0, len(trees[0])):
            cur_tree = trees[v_index, h_index]

            above = trees[:v_index, h_index]
            below = trees[v_index + 1:, h_index]
            left =  trees[v_index, :h_index]
            right = trees[v_index, h_index + 1:]
        
            if v_index != 0 and v_index != len(trees) - 1 and h_index != 0 and h_index != len(trees[0]) - 1:
                tallest = []
                tallest.append(np.amax(above, initial=0))
                tallest.append(np.amax(below, initial=0))
                tallest.append(np.amax(left, initial=0))
                tallest.append(np.amax(right, initial=0))

                lowest_obstacle = min([t for t in tallest])

                visible += 1 if trees[v_index][h_index] > lowest_obstacle else 0

                score = get_score(np.flip(above), cur_tree) * get_score(np.flip(left), cur_tree) * get_score(below, cur_tree) * get_score(right, cur_tree)

                most_scenic = score if score > most_scenic else most_scenic

print(visible)
print(most_scenic)