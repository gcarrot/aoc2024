import sys
import re
from collections import deque

# Directions: up, right, down, left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

# Function to extract integers from a string
def extract_integers(s):
    return [int(x) for x in re.findall('-?\d+', s)]

# Input file path
FILE_PATH = 'Day14/day.txt'

# Initial values for part 1 and part 2
part1_result = 0
part2_result = 0

# Read the input data
input_data = open(FILE_PATH).read().strip()

# Grid dimensions
GRID_WIDTH = 101
GRID_HEIGHT = 103

# Initialize quadrant counts
quadrant_1 = 0
quadrant_2 = 0
quadrant_3 = 0
quadrant_4 = 0

# List to store robots' data
robots = []

# Process the input data to initialize robots' positions and velocities
for line in input_data.split('\n'):
    robot_x, robot_y, velocity_x, velocity_y = extract_integers(line)
    robots.append((robot_x, robot_y, velocity_x, velocity_y))

# Simulate robot movements over time
for time_step in range(1, 10**6):
    # Create an empty grid
    grid = [['.' for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    
    if time_step == 100:
        # Reset quadrant counters at time step 100
        quadrant_1 = quadrant_2 = quadrant_3 = quadrant_4 = 0
        grid_center_x = GRID_WIDTH // 2
        grid_center_y = GRID_HEIGHT // 2

    # Move robots and update grid
    for i, (robot_x, robot_y, velocity_x, velocity_y) in enumerate(robots):
        robot_x += velocity_x
        robot_y += velocity_y
        
        # Wrap the robot around the grid if it moves out of bounds
        robot_x %= GRID_WIDTH
        robot_y %= GRID_HEIGHT
        
        robots[i] = (robot_x, robot_y, velocity_x, velocity_y)

        # Ensure the robot is within grid bounds
        assert 0 <= robot_x < GRID_WIDTH
        assert 0 <= robot_y < GRID_HEIGHT

        # Mark the robot's position on the grid
        grid[robot_y][robot_x] = '#'

        # Count the robots in the quadrants at time step 100
        if time_step == 100:
            if robot_x < grid_center_x and robot_y < grid_center_y:
                quadrant_1 += 1
            if robot_x > grid_center_x and robot_y < grid_center_y:
                quadrant_2 += 1
            if robot_x < grid_center_x and robot_y > grid_center_y:
                quadrant_3 += 1
            if robot_x > grid_center_x and robot_y > grid_center_y:
                quadrant_4 += 1

    # Part 1: Output the result at time step 100
    if time_step == 100:
        print(quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4)

    # Count the number of distinct robot groups (connected components)
    components = 0
    seen_positions = set()

    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[y][x] == '#' and (x, y) not in seen_positions:
                # Found a new component (group of connected robots)
                start_x, start_y = x, y
                components += 1
                queue = deque([(start_x, start_y)])

                while queue:
                    curr_x, curr_y = queue.popleft()

                    if (curr_x, curr_y) in seen_positions:
                        continue
                    
                    seen_positions.add((curr_x, curr_y))

                    # Check all neighboring cells for connected robots
                    for dx, dy in DIRECTIONS:
                        new_x, new_y = curr_x + dx, curr_y + dy
                        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT and grid[new_y][new_x] == '#':
                            queue.append((new_x, new_y))

    # Part 2: Output the time when there are <= 200 robot groups
    if components <= 200:
        print(time_step)

        # Print the grid at this point in time
        grid_str = [''.join(row) for row in grid]
        print('\n'.join(grid_str))
        break
