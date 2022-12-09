ASCII = 88 - 65 #X minus A
shape_score = {"rock": 1, "paper": 2, "scissors": 3}
shape = {"A": "rock", "B": "paper", "C": "scissors"}
match_score = {"win": 6, "draw": 3, "lose": 0}

def main():
    score = 0
    with open('Aoc2/input2.txt') as f:
        rounds = f.readlines()
        for round in rounds:
            round = round.strip()
            round_strat = {"opponent": shape[round[0]], "player": shape[chr(ord(round[2]) - ASCII)]}
            score += match_score[check_winner(round_strat)] + shape_score[round_strat["player"]]
    print(score)

def check_winner(roundDict):
    player = roundDict["player"]
    opponent = roundDict["opponent"]
    #Draw
    if player == opponent:
        return "draw"
    #Lose
    elif ((player, opponent) == ("rock", "paper")) or ((player, opponent) == ("paper", "scissors")) or ((player, opponent) == ("scissors", "rock")) :
        return "lose"
    #Win
    else:
        return "win"
    

main()