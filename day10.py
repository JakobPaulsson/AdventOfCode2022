def parse_input(input) -> list[int]:
    instruction_stack = []
    for instruction in input:
        if len(instruction) == 1: #noop
            instruction_stack.append(0)
        else:
            instruction_stack.append(int(instruction[1]))
    return instruction_stack

input = [l.strip().split() for l in open("i.txt")]
instruction_stack = parse_input(input)
x = 1
signal_strength = 0
cycle = 0
row = 0
current_instruction = instruction_stack.pop(0)
cycles_left = 1 if current_instruction == 0 else 2
image = [['.' for _ in range(40)] for _ in range(6)]
while True:
    if (cycle - 20) % 40 == 0:
        signal_strength += x * cycle
    cycle += 1
    if cycle % 40 == 0:
        row += 1
    current_pixel = (cycle - 1) % 40
    if cycles_left == 0:
        if len(instruction_stack) == 0:
            break
        x += current_instruction
        current_instruction = instruction_stack.pop(0)
        cycles_left = 1 if current_instruction == 0 else 2
    cycles_left -= 1
    if current_pixel == x - 1 or current_pixel == x or current_pixel == x + 1:
        image[row][current_pixel] = '#'
        
print(f"Signal Strength: {signal_strength}\n")
print('\n'.join(''.join(y for y in x) for x in image))