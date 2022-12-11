numbers =[l.strip() for l in open("i.txt")]
current =0
all_numbers = []
for number in numbers:
    current = 0 if number == "" or number == numbers[0] else current + int(number)
    all_numbers.append(current)
sum_p1 = sum((sorted(all_numbers))[-1:])
sum_p2 = sum((sorted(all_numbers))[-3:])
print("P1:", sum_p1, "P2:", sum_p2)