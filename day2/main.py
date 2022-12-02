# PART 1
opponentEnc = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

playerEnc = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

winner = {
    "Rock": "Paper",
    "Scissors": "Rock",
    "Paper": "Scissors"
}

points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "win": 6,
    "draw": 3
}

# with open("input.txt", 'r', encoding='utf-8') as file:
#     score = 0
#     for line in file:
#         choices = line.split()
#         opponent_choice = opponentEnc[choices[0]]
#         player_choice = playerEnc[choices[1]]
#         if opponent_choice == player_choice:
#             score += points["draw"] + points[player_choice]
#         elif winner[opponent_choice] == player_choice:
#             score += points["win"] + points[player_choice]
#         else:
#             score += points[player_choice]
# print(score)

# PART 2
playerEnc = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win"
}

with open("input.txt", 'r', encoding='utf-8') as file:
    score = 0
    for line in file:
        inputs = line.split()
        opponent_choice = opponentEnc[inputs[0]]
        game_outcome = playerEnc[inputs[1]]
        if game_outcome == "Draw":
            score += points["draw"] + points[opponent_choice]
        elif game_outcome == "Win":
            score += points["win"] + points[winner[opponent_choice]]
        else:
            for losing_move, winning_move in winner.items():
                if winning_move == opponent_choice:
                    score += points[losing_move]
                    break
print(score)

