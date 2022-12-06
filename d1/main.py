with open('input.txt') as fin:
    input = fin.read()

elves = []

for elf in input.split('\n\n'):
    elves.append(
        sum(
            int(calories) for calories in elf.splitlines()
        )
    )

elves.sort(reverse=True)

print(elves[0])
print(sum(elves[0:3]))