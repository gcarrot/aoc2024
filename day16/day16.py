import re
import heapq

# Direction vectors for up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse_integers_from_string(s):
    return [int(x) for x in re.findall('-?\d+', s)]

# Read input file
FILE_PATH = 'Day16/input_a.txt'
input_data = open(FILE_PATH).read().strip()

# Parse grid data
grid = input_data.split('\n')
num_rows, num_cols = len(grid), len(grid[0])

# Initialize positions for start ('S') and end ('E')
start_row, start_col, end_row, end_col = -1, -1, -1, -1
for r in range(num_rows):
    for c in range(num_cols):
        if grid[r][c] == 'S':
            start_row, start_col = r, c
        if grid[r][c] == 'E':
            end_row, end_col = r, c

# First part of the problem: Compute the shortest path from 'S' to 'E'
priority_queue = []
visited = set()
heapq.heappush(priority_queue, (0, start_row, start_col, 1))  # Starting with direction 1 (down)
start_to_cell_distances = {}
min_distance = None

while priority_queue:
    dist, row, col, dir = heapq.heappop(priority_queue)
    if (row, col, dir) not in start_to_cell_distances:
        start_to_cell_distances[(row, col, dir)] = dist
    
    if row == end_row and col == end_col and min_distance is None:
        min_distance = dist
    
    if (row, col, dir) in visited:
        continue
    visited.add((row, col, dir))
    
    dr, dc = DIRECTIONS[dir]
    next_row, next_col = row + dr, col + dc
    
    if 0 <= next_col < num_cols and 0 <= next_row < num_rows and grid[next_row][next_col] != '#':
        heapq.heappush(priority_queue, (dist + 1, next_row, next_col, dir))
    
    # Rotate direction (clockwise and counterclockwise)
    heapq.heappush(priority_queue, (dist + 1000, row, col, (dir + 1) % 4))
    heapq.heappush(priority_queue, (dist + 1000, row, col, (dir + 3) % 4))

print(min_distance)

# Second part of the problem: Compute distances from 'E' to all cells
priority_queue = []
visited = set()
for dir in range(4):
    heapq.heappush(priority_queue, (0, end_row, end_col, dir))
end_to_cell_distances = {}

while priority_queue:
    dist, row, col, dir = heapq.heappop(priority_queue)
    if (row, col, dir) not in end_to_cell_distances:
        end_to_cell_distances[(row, col, dir)] = dist
    
    if (row, col, dir) in visited:
        continue
    visited.add((row, col, dir))
    
    # Move backwards (reverse direction)
    dr, dc = DIRECTIONS[(dir + 2) % 4]
    next_row, next_col = row + dr, col + dc
    
    if 0 <= next_col < num_cols and 0 <= next_row < num_rows and grid[next_row][next_col] != '#':
        heapq.heappush(priority_queue, (dist + 1, next_row, next_col, dir))
    
    # Rotate direction (clockwise and counterclockwise)
    heapq.heappush(priority_queue, (dist + 1000, row, col, (dir + 1) % 4))
    heapq.heappush(priority_queue, (dist + 1000, row, col, (dir + 3) % 4))

# Find optimal cells that are part of the shortest path from 'S' to 'E'
valid_cells = set()
for row in range(num_rows):
    for col in range(num_cols):
        for dir in range(4):
            if (row, col, dir) in start_to_cell_distances and (row, col, dir) in end_to_cell_distances:
                if start_to_cell_distances[(row, col, dir)] + end_to_cell_distances[(row, col, dir)] == min_distance:
                    valid_cells.add((row, col))

print(len(valid_cells))
