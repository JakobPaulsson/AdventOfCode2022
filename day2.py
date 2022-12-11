rounds = [l.strip().split() for l in open("i.txt")]

score = 0
score_choice = {"X": 1, "Y": 2, "Z": 3}
win = {"X": "C", "Y": "A", "Z": "B"}
draw = {"X": "A", "Y": "B", "Z": "C"}

score_2 = 0
win_2 = {"A": "Y", "B": "Z", "C": "X"}
draw_2 = {"A": "X", "B": "Y", "C": "Z"}
lose_2 = {"A": "Z", "B": "X", "C": "Y"}

for round in rounds:
    score += score_choice[round[1]]
    if draw[round[1]] == round[0]:
        score += 3
    elif win[round[1]] == round[0]:
        score += 6
    if round[1] == "X":
        score_2 += score_choice[lose_2[round[0]]]
    elif round[1] == "Y":
        score_2 += score_choice[draw_2[round[0]]]
        score_2 += 3
    else:
        score_2 += score_choice[win_2[round[0]]]
        score_2 += 6

print("P1:", score)
print("P2:", score_2)
