def parse_crates(input, crate_list, number_of_crates) -> int:
    line = 0
    while(not input[line][1] == '1'):
        for i in range(number_of_crates):
            crate_index = 1 + 4*i
            if not input[line][crate_index] == ' ':
                crate_list[i].append(input[line][crate_index])
        line += 1
    return line + 2

def parse_and_move_crates_preserve_order(input, crate_list):
    for instruction in input:
        move_amount, move_from, move_to = [int(x) for x in instruction.split(' ') if x.isnumeric()]
        temp = []
        for _ in range(move_amount):
            temp.append(crate_list[move_from - 1].pop(0))
        temp.extend(crate_list[move_to - 1])
        crate_list[move_to - 1] = temp

def parse_and_move_crates(input, crate_list):
    for instruction in input:
        move_amount, move_from, move_to = [int(x) for x in instruction.split(' ') if x.isnumeric()]
        for _ in range(move_amount):
            crate_list[move_to - 1].insert(0, crate_list[move_from - 1].pop(0))

def print_crates(crate_list, number_of_crates):
    for i in range(number_of_crates):
        print(crate_list[i][0], end="")

input = [l.strip('\n') for l in open("i.txt")]
number_of_crates = int(len(input[0]) / 4) + 1

#P1
crate_list = [[] for _ in range(number_of_crates)]
line = parse_crates(input, crate_list, number_of_crates)
parse_and_move_crates(input[line:], crate_list)
print_crates(crate_list, number_of_crates)
print()

#P2
crate_list = [[] for _ in range(number_of_crates)]
line = parse_crates(input, crate_list, number_of_crates)
parse_and_move_crates_preserve_order(input[line:], crate_list)
print_crates(crate_list, number_of_crates)