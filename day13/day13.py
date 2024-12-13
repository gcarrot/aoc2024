import time

FILE_PATH = 'Day13/day.txt'
start_time = time.time()
with open(FILE_PATH) as file:
    lines = file.read().strip().split('\n')


def parse_line(line):
    tokens = line.split()
    if line.startswith("Button"):
        label = tokens[1].split(":")[0]
        x_value = int(tokens[2][2:-1])
        y_value = int(tokens[3][2:])
        return label, x_value, y_value
    elif line.startswith("Prize"):
        prize_x = int(tokens[1][2:-1])
        prize_y = int(tokens[2][2:])
        return prize_x, prize_y
    return None

def solve(part: int):
    tokens_count = 0
    add_value = 10000000000000 if part == 2 else 0

    x1, y1, x2, y2 = None, None, None, None

    for line in lines:
        parsed_data = parse_line(line.strip())
        
        if parsed_data:
            if len(parsed_data) == 3:  # Button line
                label, x_value, y_value = parsed_data
                if label == 'A':
                    x1, y1 = x_value, y_value
                else:
                    x2, y2 = x_value, y_value
            elif len(parsed_data) == 2:  # Prize line
                prize_x, prize_y = parsed_data
                prize_x += add_value
                prize_y += add_value
                
                # Calculate the coefficients for the equation
                coeff = x1 * y2 - y1 * x2
                if coeff != 0:
                    a = (prize_x * y2 - prize_y * x2) / coeff
                    b = (prize_y * x1 - prize_x * y1) / coeff
                    if a.is_integer() and b.is_integer():
                        tokens_count += int(3 * a + b)

    print(tokens_count)

solve(1)
solve(2)

end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")