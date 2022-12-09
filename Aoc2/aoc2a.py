ASCII = 88 - 65 #X minus A
shape_score = {"rock": 1, "paper": 2, "scissors": 3}
shape = {"A": "rock", "B": "paper", "C": "scissors"}
match_score = {"win": 6, "draw": 3, "lose": 0}
result = {"X": "lose", "Y": "draw", "Z": "win"}

def main():
    score = 0
    with open('Aoc2/input2.txt') as f:
        rounds = f.readlines()
        for round in rounds:
            round = round.strip()
            round_strat = {"opponent": shape[round[0]], "result": result[round[2]]}
            print(round_strat["result"], match_score[round_strat["result"]], "opponent=", round_strat["opponent"], "player=", player_plays(round_strat), shape_score[player_plays(round_strat)])
            score += match_score[round_strat["result"]] + shape_score[player_plays(round_strat)]
    print(score)

def player_plays(roundDict):
    result = roundDict["result"] #win, lose, draw
    opponent = roundDict["opponent"] #rock, paper, scissors
    #Draw
    if result == "draw":
        return opponent
    #Lose
    elif result == "lose":
        if opponent == "rock":
            return "scissors"
        elif opponent == "paper":
            return "rock"
        else:
            return "paper"
    #Win
    else:
        if opponent == "rock":
            return "paper"
        elif opponent == "paper":
            return "scissors"
        else:
            return "rock"
main()