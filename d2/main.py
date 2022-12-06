with open('input.txt') as fin:
    input = fin.read()

score = 0

def get_winning_play(played):
    if played == 'C':
        return 'A'
    else:
        return chr(ord(played) + 1)

for game in input.splitlines():
    played = game[0]
    plan = game[2]

    match plan:
        case 'X':
            # lose
            score += ord(
                get_winning_play(
                    get_winning_play(played)
                )
            )
        case 'Y':
            # draw
            score += ord(played) + 3
        case 'Z':
            # win
            score += ord(
                get_winning_play(played)
            ) + 6
    score -= 64

print(score)
