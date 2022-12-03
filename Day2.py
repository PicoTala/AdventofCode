round_outcomes = []

with open('day2_input.txt') as rps_results:
    for line in rps_results:
        player1 = line[0:1]
        print(player1)
        player2 = line[2:3]
        print(player2)
        if player1 == 'A':
            if player2 == 'X':
                print("Draw")
                round_outcomes.append(int(4))
            if player2 == 'Y':
                print("Win")
                round_outcomes.append(int(8))
            if player2 == 'Z':
                print("Lose")
                round_outcomes.append(int(3))
        if player1 == 'B':
            if player2 == 'X':
                print("Lose")
                round_outcomes.append(int(1))
            if player2 == 'Y':
                print("Draw")
                round_outcomes.append(int(5))
            if player2 == 'Z':
                print("Win")
                round_outcomes.append(int(9))
        if player1 == 'C':
            if player2 == 'X':
                print("Win")
                round_outcomes.append(int(7))
            if player2 == 'Y':
                print("Lose")
                round_outcomes.append(int(2))
            if player2 == 'Z':
                print("Draw")
                round_outcomes.append(int(6))
print(sum(round_outcomes))

# part two of day two

# X means lose, Y means a draw, Z means win

round_out_shapes = []

# create new list for these results, reopen file

with open('day2_input.txt') as rps_results:
    for line in rps_results:
        player1 = line[0:1]
        print(player1)
        player2 = line[2:3]
        print(player2)
        if player1 == 'A':
            if player2 == 'X':
                print("Lose: Pick Scissors")
                round_out_shapes.append(int(3))
            if player2 == 'Y':
                print("Draw: Pick Rock")
                round_out_shapes.append(int(4))
            if player2 == 'Z':
                print("Win: Pick Paper")
                round_out_shapes.append(int(8))
        if player1 == 'B':
            if player2 == 'X':
                print("Lose: Pick Rock")
                round_out_shapes.append(int(1))
            if player2 == 'Y':
                print("Draw: Pick Paper")
                round_out_shapes.append(int(5))
            if player2 == 'Z':
                print("Win: Pick Scissors")
                round_out_shapes.append(int(9))
        if player1 == 'C':
            if player2 == 'X':
                print("Lose: Pick Paper")
                round_out_shapes.append(int(2))
            if player2 == 'Y':
                print("Draw: Pick Scissors")
                round_out_shapes.append(int(6))
            if player2 == 'Z':
                print("Win: Pick Rock")
                round_out_shapes.append(int(7))

print(sum(round_out_shapes))
