def parse_ls(line, input, sizes):
    directory_size = 0
    while not input[line+1][0] == '$':
        line += 1
        commands = input[line].split(' ')
        if commands[0] == 'dir':
            continue
        directory_size += int(commands[0])
    for key in sizes:
        if not sizes[key]["finished"]:
            sizes[key]["size"] += directory_size
    return line + 1

def parse_cd(current_directory, line, sizes, total_size, commands):
    if commands[2] == '..':
        for key, value in list(sizes.items()):
            sizes[key]["level"] -= 1
            if sizes[key]["finished"] or not value["level"] == 0:
                continue
            if value["size"] < 100000:
                total_size += value["size"]
            sizes[key]["finished"] = True
        return current_directory, line + 1, total_size
    
    prev_directory = current_directory
    current_directory = commands[2]
    sizes[prev_directory + "-" + current_directory] = {"size": 0, "level": 0, "finished": False}

    for key, value in sizes.items():
        sizes[key]["level"] += 1
    
    return current_directory, line + 1, total_size

input = [l.strip() for l in open('i.txt')] + ["$ cd .."]
line = 0
total_size = 0
current_directory = ""
sizes = {}
while line < len(input):
    commands = input[line].split(' ')
    if commands[1] == 'ls':
        line = parse_ls(line, input, sizes)
        continue
    current_directory, line, total_size = parse_cd("", line, sizes, total_size, commands)

print("P1:", total_size)

needed_space = 30000000 - (70000000 - sizes["-/"]["size"])
sizes = sorted([x["size"] for x in sizes.values()])
for size in sizes:
    if size > needed_space:
        print("P2:", size)
        break