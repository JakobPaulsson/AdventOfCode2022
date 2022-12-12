def parse_input(input):
    grid = [[0] * len(input[0]) for _ in range(len(input))]
    start, end = tuple(), tuple()
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                start = (x, y)
                continue
            if input[y][x] == 'E':
                end = (x, y)
                grid[y][x] = 25
                continue
            grid[y][x] = ord(input[y][x]) - ord('a')
    return start, end, grid


def visit_cell(x_old, y_old, x_visit, y_visit, grid, cost_grid, visited):
    if x_visit == -1 or y_visit == -1 or x_visit == len(grid[0]) or y_visit == len(grid):
        return []
    if not visited[y_visit][x_visit] and grid[y_old][x_old] + 1 >= grid[y_visit][x_visit]:
        cost_grid[y_visit][x_visit] += cost_grid[y_old][x_old] + 1
        visited[y_visit][x_visit] = True
        return [(x_visit, y_visit)]
    return []


def visit_surrounding(x, y, grid, cost_grid, visited):
    cells_to_visit = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        cells_to_visit += visit_cell(x, y, x+dx, y+dy, grid, cost_grid, visited)
    return cells_to_visit


def get_starting_cells(grid):
    starting_cells = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                starting_cells.append((x, y))
    return starting_cells


def visit_all_cells(grid, cost_grid, visited, starting_cell):
    visit_queue = [starting_cell]
    while True:
        visit_queue += visit_surrounding(visit_queue[0][0], visit_queue[0][1], grid, cost_grid, visited)
        visit_queue.pop(0)
        if len(visit_queue) == 0:
            return


input = [l.strip() for l in open("i.txt")]
start, end, grid = parse_input(input)
costs = []
for starting_cell in get_starting_cells(grid):
    cost_grid = [[0] * len(input[0]) for _ in range(len(input))]
    visited = [[False] * len(input[0]) for _ in range(len(input))]
    visited[starting_cell[1]][starting_cell[0]] = True
    visit_all_cells(grid, cost_grid, visited, starting_cell)
    cost = cost_grid[end[1]][end[0]]
    if not cost == 0:
        costs.append(cost)
print("P1:", costs[0])
print("P2:", min(costs))
