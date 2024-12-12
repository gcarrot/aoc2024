
from collections import deque, defaultdict


# Constants
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
FILE_PATH = 'Day12/day.txt'

# Read and process the input file
with open(FILE_PATH) as file:
    grid = file.read().strip().split('\n')

num_rows = len(grid)
num_cols = len(grid[0])

visited = set()  # To track visited positions
total_area_perimeter = 0
total_area_sides = 0

# Function to perform a BFS search to calculate area and perimeter
def bfs_area_perimeter(start_row, start_col):
    queue = deque([(start_row, start_col)])
    area = 0
    perimeter = 0
    perimeter_neighbors = defaultdict(set)

    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        area += 1

        for dr, dc in DIRECTIONS:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] == grid[row][col]:
                queue.append((new_row, new_col))
            else:
                perimeter += 1
                perimeter_neighbors[(dr, dc)].add((row, col))

    # Calculate the additional perimeter sides based on neighboring cells
    total_sides = 0
    for direction, positions in perimeter_neighbors.items():
        visited_perimeter = set()
        for pr, pc in positions:
            if (pr, pc) not in visited_perimeter:
                total_sides += 1
                sub_queue = deque([(pr, pc)])
                while sub_queue:
                    r, c = sub_queue.popleft()
                    if (r, c) in visited_perimeter:
                        continue
                    visited_perimeter.add((r, c))
                    for dr, dc in DIRECTIONS:
                        rr, cc = r + dr, c + dc
                        if (rr, cc) in positions:
                            sub_queue.append((rr, cc))

    return area, perimeter, total_sides

# Iterate through the grid to calculate total area, perimeter, and sides
for row in range(num_rows):
    for col in range(num_cols):
        if (row, col) not in visited:
            area, perimeter, sides = bfs_area_perimeter(row, col)
            total_area_perimeter += area * perimeter
            total_area_sides += area * sides

# Output the results
print(total_area_perimeter)
print(total_area_sides)