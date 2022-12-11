def move_T(T_pos, H_pos_moved):
    if T_pos[0] == H_pos_moved[0] - 2 and T_pos[1] == H_pos_moved[1] - 2:
        return [H_pos_moved[0]-1, H_pos_moved[1]-1]
    elif T_pos[0] == H_pos_moved[0] - 2 and T_pos[1] == H_pos_moved[1] + 2:
        return [H_pos_moved[0]-1, H_pos_moved[1]+1]
    elif T_pos[0] == H_pos_moved[0] + 2 and T_pos[1] == H_pos_moved[1] - 2:
        return [H_pos_moved[0]+1, H_pos_moved[1]-1]
    elif T_pos[0] == H_pos_moved[0] + 2 and T_pos[1] == H_pos_moved[1] + 2:
        return [H_pos_moved[0]+1, H_pos_moved[1]+1]
    elif T_pos[1] == H_pos_moved[1] + 2:
        return [H_pos_moved[0], H_pos_moved[1]+1]
    elif T_pos[1] == H_pos_moved[1] - 2:
        return [H_pos_moved[0], H_pos_moved[1]-1]
    elif T_pos[0] == H_pos_moved[0] + 2:
        return [H_pos_moved[0]+1, H_pos_moved[1]]
    elif T_pos[0] == H_pos_moved[0] - 2:
        return [H_pos_moved[0]-1, H_pos_moved[1]]
    return T_pos


input = [l.strip() for l in open("i.txt")]
H_pos = [0, 0]
T_pos = [0, 0]
visited = (set(), set())
positions = [[0, 0] for _ in range(10)]

for line in input:
    direction, amount = line.split()
    for step in range(int(amount)):
        if direction == 'U':
            positions[0][1] += 1
        if direction == 'R':
            positions[0][0] += 1
        if direction == 'L':
            positions[0][0] -= 1
        if direction == 'D':
            positions[0][1] -= 1
        for i in range(1, 10):
            positions[i] = move_T(positions[i], positions[i-1])

        visited[0].add(str(positions[1][0])+str(positions[1][1]))
        visited[1].add(str(positions[9][0])+str(positions[9][1]))

print("P1:", len(visited[0]))
print("P2:", len(visited[1]))
