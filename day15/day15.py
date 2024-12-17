import re
from collections import deque

# Direction offsets for up, right, down, and left movements
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Function to extract integers from a string
def extract_integers(s):
    return [int(x) for x in re.findall('-?\d+', s)]

# Read the input data from the file
FILE_PATH = 'Day15/day.txt'
input_data = open(FILE_PATH).read().strip()

# Split the input data into the grid and instructions
grid_data, instructions = input_data.split('\n\n')
grid = grid_data.split('\n')

# Function to solve the puzzle
def solve(grid, is_part2):
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Copy the grid (this is redundant since it's already in a list of lists format)
    grid = [list(row) for row in grid]

    # Part 2: Expand the grid
    if is_part2:
        expanded_grid = []
        for row in grid:
            expanded_row = []
            for cell in row:
                if cell == '#':
                    expanded_row.extend(['#', '#'])
                elif cell == 'O':
                    expanded_row.extend(['[', ']'])
                elif cell == '.':
                    expanded_row.extend(['.', '.'])
                elif cell == '@':
                    expanded_row.extend(['@', '.'])
            expanded_grid.append(expanded_row)
        grid = expanded_grid
        cols *= 2  # Update column count for the expanded grid

    # Find the starting position of the '@' symbol
    start_row, start_col = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                start_row, start_col = r, c
                grid[r][c] = '.'  # Mark the start as a free space
                break
        if start_row is not None:
            break

    # Process each instruction
    row, col = start_row, start_col
    for instruction in instructions:
        if instruction == '\n':  # Skip newlines
            continue

        # Determine the direction of movement based on the instruction
        direction_offsets = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
        delta_row, delta_col = direction_offsets[instruction]

        # Calculate new position after moving
        new_row, new_col = row + delta_row, col + delta_col

        # Check if the new position is valid
        if grid[new_row][new_col] == '#':
            continue  # Hit a wall, stay in the same position
        elif grid[new_row][new_col] == '.':
            row, col = new_row, new_col  # Move to the new position
        elif grid[new_row][new_col] in ['[', ']', 'O']:
            # Handle complex cells (like '[', ']', or 'O')
            queue = deque([(row, col)])
            visited = set()
            is_valid_move = True

            while queue:
                cur_row, cur_col = queue.popleft()

                if (cur_row, cur_col) in visited:
                    continue
                visited.add((cur_row, cur_col))

                next_row, next_col = cur_row + delta_row, cur_col + delta_col

                if grid[next_row][next_col] == '#':
                    is_valid_move = False
                    break
                if grid[next_row][next_col] in ['O', '[']:
                    queue.append((next_row, next_col))
                if grid[next_row][next_col] == ']':
                    queue.append((next_row, next_col))

            if not is_valid_move:
                continue  # If the move isn't valid, stay at the current position

            # Update the grid with the new positions
            while visited:
                for cur_row, cur_col in sorted(visited):
                    next_row, next_col = cur_row + delta_row, cur_col + delta_col
                    if (next_row, next_col) not in visited:
                        assert grid[next_row][next_col] == '.'
                        grid[next_row][next_col] = grid[cur_row][cur_col]
                        grid[cur_row][cur_col] = '.'
                        visited.remove((cur_row, cur_col))

            row, col = row + delta_row, col + delta_col  # Update position after move

    # Calculate the final result
    result = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['[', 'O']:
                result += 100 * r + c  # Add weighted position to result

    return result

# Solve for both parts
print(solve(grid, False))  # Part 1 1514333
print(solve(grid, True))   # Part 2 1528453





