def main():
    file = open("input.txt", "r");
    turn_score = [];
    outcomes = {"A": {"X": 3, "Y": 4, "Z": 8}, "B": {"X": 1, "Y": 5, "Z": 9}, "C": {"X": 2, "Y": 6, "Z": 7}};

    for turn in file:   
        score = 0;    
        strategy = turn.strip().split(" ");
        score = outcomes[strategy[0]][strategy[1]]
        turn_score.append(score);

    file.close();
    return sum(turn_score);
    
print(main());
