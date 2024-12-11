from collections import deque

# Read file content
with open('Day9/day9.txt') as file:
    file_content = file.read().strip()

# Split file content into lines
lines = file_content.split('\n')

def solve(part2):
    file_positions = deque()  # Stores positions and file IDs
    available_spaces = deque()  # Stores space positions and sizes
    current_file_id = 0
    result = []  # Final output list
    current_position = 0  # Current position in result

    # Iterate over the file content
    for i, c in enumerate(file_content):
        if i % 2 == 0:  # Even index means a new file (file_positions part)
            if part2:
                file_positions.append((current_position, int(c), current_file_id))
            for _ in range(int(c)):
                result.append(current_file_id)
                if not part2:
                    file_positions.append((current_position, 1, current_file_id))
                current_position += 1
            current_file_id += 1
        else:  # Odd index means a space (available_spaces part)
            available_spaces.append((current_position, int(c)))
            for _ in range(int(c)):
                result.append(None)  # Fill with None for space
                current_position += 1

    # Move files into available spaces, checking from the back
    for current_position, space_size, current_file_id in reversed(file_positions):
        for space_idx, (space_pos, space_sz) in enumerate(available_spaces):
            if space_pos < current_position and space_size <= space_sz:
                for i in range(space_size):
                    assert result[current_position + i] == current_file_id, f'Unexpected value at {current_position+i}'
                    result[current_position + i] = None
                    result[space_pos + i] = current_file_id
                available_spaces[space_idx] = (space_pos + space_size, space_sz - space_size)
                break

    # Calculate the final answer
    ans = sum(i * c for i, c in enumerate(result) if c is not None)
    
    return ans

# Solve both parts
p1 = solve(False)
p2 = solve(True)

# Print the results
print(p1)
print(p2)
