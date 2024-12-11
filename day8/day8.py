from collections import defaultdict
from itertools import combinations

# Initialize dictionary to store antennas' positions (using complex numbers)
antennas = defaultdict(list)

# Initialize maximum row and column values
max_row = 0
max_col = 0

# Read the file and store antennas' positions
with open('Day8/day8.txt') as f:
    for row_index, line in enumerate(f):
        max_row = max(max_row, row_index)  # Update maximum row index
        for col_index, char in enumerate(line.strip()):
            max_col = max(max_col, col_index)  # Update maximum column index
            if char != ".":
                antennas[char].append(complex(f"{row_index}+{col_index}j"))

# Initialize sets to store anti nodes for part 1 and part 2
part1_anti_nodes = set()
part2_anti_nodes = set()

# Process each antenna to calculate anti nodes
for antenna in antennas:
    # Generate combinations of antenna pairs for distance calculations
    for antenna1, antenna2 in combinations(antennas[antenna], 2):
        # Calculate the distance between two antennas
        distance = antenna2 - antenna1

        # Generate possible anti nodes in both directions
        anti_nodes1 = [
            antenna2 + distance * n for n in range(1, 100)
            if (0 <= (antenna2 + distance * n).real <= max_row)
            and (0 <= (antenna2 + distance * n).imag <= max_col)
        ]
        anti_nodes2 = [
            antenna1 - distance * n for n in range(1, 100)
            if (0 <= (antenna1 - distance * n).real <= max_row)
            and (0 <= (antenna1 - distance * n).imag <= max_col)
        ]

        # Part 1: Only take the first anti node in each direction
        part1_anti_nodes |= {*anti_nodes1[:1]}  # Add the first anti node from direction 1
        part1_anti_nodes |= {*anti_nodes2[:1]}  # Add the first anti node from direction 2

        # Part 2: Take all generated anti nodes
        part2_anti_nodes |= {*anti_nodes1}  # Add all anti nodes from direction 1
        part2_anti_nodes |= {*anti_nodes2}  # Add all anti nodes from direction 2

        # Include the antennas themselves in part 2 anti nodes
        part2_anti_nodes |= {*[antenna1, antenna2]}  # Add the pair of antennas

# Calculate the total number of anti nodes for both parts
result_part1 = len(part1_anti_nodes)
result_part2 = len(part2_anti_nodes)

# Output the results
print(result_part1)
print(result_part2)