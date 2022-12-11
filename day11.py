def parse_monkeys(input) -> dict:
    monkeys = {}
    for line in input:
        if line[0] == 'Monkey':
            current_monkey = int(line[1][0])
            monkeys[current_monkey] = {'inspected': 0}
        if line[0] == 'Starting':
            items = []
            for i in range(2, len(line)):
                items.append(int(line[i].strip(',')))
            monkeys[current_monkey]['items'] = items
        if line[0] == 'Operation:':
            monkeys[current_monkey]['operator'] = line[4]
            monkeys[current_monkey]['number1'] = line[3]
            monkeys[current_monkey]['number2'] = line[5]
        if line[0] == 'Test:':
            monkeys[current_monkey]['divisor'] = int(line[3])
        if line[1] == 'true:':
            monkeys[current_monkey]['true'] = int(line[5])
        if line[1] == 'false:':
            monkeys[current_monkey]['false'] = int(line[5])
    return monkeys


def inspect_item(monkey_number, monkeys, should_divide):
    op = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}
    for item in monkeys[monkey_number]['items']:
        monkeys[monkey_number]['inspected'] += 1
        number1 = monkeys[monkey_number]['number1']
        number2 = monkeys[monkey_number]['number2']
        number1 = item if monkeys[monkey_number]['number1'] == 'old' else int(monkeys[monkey_number]['number1'])
        number2 = item if monkeys[monkey_number]['number2'] == 'old' else int(monkeys[monkey_number]['number2'])
        new_item = op[monkeys[monkey_number]['operator']](number1, number2)
        if should_divide:
            new_item = new_item // 3
        new_item = reduce_number([2, 3, 7, 11, 19, 13,  5, 17], new_item)
        if new_item % monkeys[monkey_number]['divisor'] == 0:
            monkeys[monkeys[monkey_number]['true']]['items'].append(new_item)
        else:
            monkeys[monkeys[monkey_number]['false']]['items'].append(new_item)
    monkeys[monkey_number]['items'].clear()


def reduce_number(factors, number):
    number_to_reduce_with = 1
    for factor in factors:
        number_to_reduce_with *= factor
    return number % number_to_reduce_with


def inspect_all_items(monkeys, should_divide):
    for monkey in monkeys:
        inspect_item(monkey, monkeys, should_divide)


input = [l.strip().split() for l in open("i.txt") if not len(l.strip()) == 0]
monkeys = parse_monkeys(input)
monkeys2 = parse_monkeys(input)

for i in range(20):
    inspect_all_items(monkeys, should_divide=True)
for i in range(10000):
    inspect_all_items(monkeys2, should_divide=False)

sorted_inspected = sorted([monkeys[monkey]['inspected'] for monkey in monkeys])
sorted_inspected2 = sorted([monkeys2[monkey]['inspected'] for monkey in monkeys2])

print("Part 1:", sorted_inspected[-1] * sorted_inspected[-2])
print("Part 2:", sorted_inspected2[-1] * sorted_inspected2[-2])
