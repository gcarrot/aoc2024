file_content = open('Day7/day7.txt').read().strip()
lines = file_content.split('\n')

# Initialize part 1 and part 2 results
result_part1 = 0
result_part2 = 0

# Function to check if the target is valid for the given numbers
def is_valid(target, numbers, concat):
    # If there's only one number left, check if it matches the target
    if len(numbers) == 1:
        return numbers[0] == target
    
    # Try combining the first two numbers (addition and multiplication) and check recursively
    if is_valid(target, [numbers[0] + numbers[1]] + numbers[2:], concat):
        return True
    if is_valid(target, [numbers[0] * numbers[1]] + numbers[2:], concat):
        return True
    
    # If concatenation is allowed, try combining the first two numbers as a concatenated integer
    if concat and is_valid(target, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], concat):
        return True
    
    return False

# Process each line
for line in lines:
    target_str, numbers_str = line.strip().split(':')
    target = int(target_str)
    numbers = [int(x) for x in numbers_str.strip().split()]

    # Check if the target is valid for part 1 and part 2
    if is_valid(target, numbers, concat=False):
        result_part1 += target
    if is_valid(target, numbers, concat=True):
        result_part2 += target

# Print results for part 1 and part 2
print(result_part1)
print(result_part2)