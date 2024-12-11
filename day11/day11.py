from collections import Counter

# Read file content and split into lines
with open('Day11/day.txt') as file:
    lines = file.read().strip().split()

# Function to apply transformation rules
def transform(counts):
    new_counts = Counter()
    for s, cnt in counts.items():
        if s == "0":
            # Rule 1: If the stone is "0", convert it to "1"
            new_counts["1"] += cnt
        else:
            # Precompute the number of digits and handle transformations
            digits = len(s)
            if digits % 2 == 0:
                # Rule 2: Split the number if it has an even number of digits
                half = digits // 2
                left_part, right_part = str(int(s[:half])), str(int(s[half:]))
                new_counts[left_part] += cnt
                new_counts[right_part] += cnt
            else:
                # Rule 3: Multiply the number by 2024 if it has an odd number of digits
                new_counts[str(int(s) * 2024)] += cnt
    return new_counts

# Initialize the count of stones
counts = Counter(lines)

# Apply transformations and track results only at required steps
for i in range(75):
    counts = transform(counts)
    if i == 24 or i == 74:  # After 25 or 75 transformations
        print(f"After {i + 1} transformations: {sum(counts.values())}")
