
from collections import defaultdict, Counter, deque
file_content = open('Day10/day.txt').read().strip()
lines = file_content.split('\n')

# Convert the input lines into a 2D grid of integers
grid = [[int(x) for x in row] for row in lines]

# Dimensions of the grid
rows = len(grid)
cols = len(grid[0])

# This will hold the results for both parts
part1_result = 0
part2_result = 0

# Directions for moving in the grid (up, right, down, left)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def count_zeros_from_start(row, col):
    """
    Counts how many different 0s can be reached by going down 
    from the starting point (row, col).
    """
    queue = deque([(row, col)])
    visited = set()
    zero_count = 0

    while queue:
        current_row, current_col = queue.popleft()

        # Skip if this cell has already been visited
        if (current_row, current_col) in visited:
            continue
        
        visited.add((current_row, current_col))

        # Increment the count if the current cell value is 0
        if grid[current_row][current_col] == 0:
            zero_count += 1

        # Explore all possible directions (up, right, down, left)
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            # Check if the new position is within the grid bounds 
            # and if the value is one less than the current cell value
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == grid[current_row][current_col] - 1:
                queue.append((new_row, new_col))

    return zero_count

# Memoization dictionary for part 2
memo = {}

def count_paths_to_zero(row, col):
    """
    Counts how many distinct paths from (row, col) lead to a 0, 
    where each path follows the condition that each step moves to a cell 
    with a value exactly 1 less than the current cell value.
    """
    # Base case: if the current cell is 0, there is exactly 1 path
    if grid[row][col] == 0:
        return 1

    # Return the result if it has already been computed
    if (row, col) in memo:
        return memo[(row, col)]

    path_count = 0

    # Explore all possible directions
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within the grid bounds 
        # and if the value is one less than the current cell value
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == grid[row][col] - 1:
            path_count += count_paths_to_zero(new_row, new_col)

    # Memoize the result for the current cell
    memo[(row, col)] = path_count
    return path_count

# Iterate through every cell in the grid
for r in range(rows):
    for c in range(cols):
        # When the cell value is 9, apply both parts of the problem
        if grid[r][c] == 9:
            part1_result += count_zeros_from_start(r, c)
            part2_result += count_paths_to_zero(r, c)

# Output the results for both parts
print(part1_result)
print(part2_result)