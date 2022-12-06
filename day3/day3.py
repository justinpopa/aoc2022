
def part_one(input):
    sum = 0

    for rucksack in input.splitlines():
        midpoint = len(rucksack) // 2

        letter = ord(
            ''.join(
                set(rucksack[:midpoint]).intersection(rucksack[midpoint:])
            )
        )

        priority = letter - 96 if letter >= 97 else letter - 38

        sum += priority
    
    return sum

def part_two(input):
    raw = input.splitlines()

    groups = []

    for line in range(0, len(raw), 3):
        groups.append(f'{raw[line]}\n{raw[line + 1]}\n{raw[line + 2]}')

    sum = 0
    for line in groups:
        divided = line.splitlines()
        letter = ''.join(
            set(divided[0]).intersection(divided[1], divided[2])
        )

        priority = ord(letter) - 96 if ord(letter) >= 97 else ord(letter) - 38

        sum += priority

    return sum

with open('input.txt') as fin:
    input = fin.read()
    print(
        f'Day 3 - First Half: {part_one(input)}'
    )
    print(
        f'Day 3 - Second Half: {part_two(input)}'
    )