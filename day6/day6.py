from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)

input = puzzle.input_data

def find_first_distinct_set_of_x(string, length):
    for i in range(len(input)):
        if len(''.join(set(input[i - length:i]))) == length:
            return i

print(find_first_distinct_set_of_x(input, 4))
print(find_first_distinct_set_of_x(input, 14))