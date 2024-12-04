
file = open('Day4/day4.txt').read().strip()

p1 = 0
p2 = 0

lines = file.split('\n')
sizeY = len(lines)
sizeX = len(lines[0])
for y in range(sizeY):
    for x in range(sizeX):

        
        if x+3<sizeX and lines[y][x]=='X' and lines[y][x+1]=='M' and lines[y][x+2]=='A' and lines[y][x+3]=='S':
            p1 += 1
        if y+3<sizeX and lines[y][x]=='X' and lines[y+1][x]=='M' and lines[y+2][x]=='A' and lines[y+3][x]=='S':
            p1 += 1
        if y+3<sizeX and x+3<sizeX and lines[y][x]=='X' and lines[y+1][x+1]=='M' and lines[y+2][x+2]=='A' and lines[y+3][x+3]=='S':
            p1 += 1
        if x+3<sizeX and lines[y][x]=='S' and lines[y][x+1]=='A' and lines[y][x+2]=='M' and lines[y][x+3]=='X':
            p1 += 1
        if y+3<sizeY and lines[y][x]=='S' and lines[y+1][x]=='A' and lines[y+2][x]=='M' and lines[y+3][x]=='X':
            p1 += 1
        if y+3<sizeY and x+3<sizeX and lines[y][x]=='S' and lines[y+1][x+1]=='A' and lines[y+2][x+2]=='M' and lines[y+3][x+3]=='X':
            p1 += 1
        if y-3>=0 and x+3<sizeX and lines[y][x]=='S' and lines[y-1][x+1]=='A' and lines[y-2][x+2]=='M' and lines[y-3][x+3]=='X':
            p1 += 1
        if y-3>=0 and x+3<sizeX and lines[y][x]=='X' and lines[y-1][x+1]=='M' and lines[y-2][x+2]=='A' and lines[y-3][x+3]=='S':
            p1 += 1

        if y+2<sizeY and x+2<sizeX and lines[y][x]=='M' and lines[y+1][x+1]=='A' and lines[y+2][x+2]=='S' and lines[y+2][x]=='M' and lines[y][x+2]=='S':
            p2 += 1
        if y+2<sizeY and x+2<sizeX and lines[y][x]=='M' and lines[y+1][x+1]=='A' and lines[y+2][x+2]=='S' and lines[y+2][x]=='S' and lines[y][x+2]=='M':
            p2 += 1
        if y+2<sizeY and x+2<sizeX and lines[y][x]=='S' and lines[y+1][x+1]=='A' and lines[y+2][x+2]=='M' and lines[y+2][x]=='M' and lines[y][x+2]=='S':
            p2 += 1
        if y+2<sizeY and x+2<sizeX and lines[y][x]=='S' and lines[y+1][x+1]=='A' and lines[y+2][x+2]=='M' and lines[y+2][x]=='S' and lines[y][x+2]=='M':
            p2 += 1

print(p1)
print(p2)

def check_p1_patterns(lines, y, x, sizeX, sizeY):
    p1 = 0

    # Helper function to check if the coordinates are within bounds
    def in_bounds(y, x):
        return 0 <= y < sizeY and 0 <= x < sizeX

    # Define the patterns for XMAS and SAMX
    patterns = [
        ('X', 'M', 'A', 'S'),  # XMAS pattern
        ('S', 'A', 'M', 'X')   # SAMX pattern
    ]

    # Loop through the patterns
    for pattern in patterns:
        # Horizontal check
        if in_bounds(y, x + 3):
            if (lines[y][x] == pattern[0] and 
                lines[y][x + 1] == pattern[1] and 
                lines[y][x + 2] == pattern[2] and 
                lines[y][x + 3] == pattern[3]):
                p1 += 1

        # Vertical check
        if in_bounds(y + 3, x):
            if (lines[y][x] == pattern[0] and 
                lines[y + 1][x] == pattern[1] and 
                lines[y + 2][x] == pattern[2] and 
                lines[y + 3][x] == pattern[3]):
                p1 += 1

        # Diagonal check (bottom-right)
        if in_bounds(y + 3, x + 3):
            if (lines[y][x] == pattern[0] and 
                lines[y + 1][x + 1] == pattern[1] and 
                lines[y + 2][x + 2] == pattern[2] and 
                lines[y + 3][x + 3] == pattern[3]):
                p1 += 1

        # Diagonal check (top-right)
        if in_bounds(y - 3, x + 3):
            if (lines[y][x] == pattern[0] and 
                lines[y - 1][x + 1] == pattern[1] and 
                lines[y - 2][x + 2] == pattern[2] and 
                lines[y - 3][x + 3] == pattern[3]):
                p1 += 1

    return p1

def check_p2_patterns(lines, y, x, sizeX, sizeY):
    p2 = 0
    
    # Check if we are within bounds for all necessary positions
    if y + 2 < sizeY and x + 2 < sizeX:
        # Collect the values at the positions we care about
        val1, val2, val3 = lines[y][x], lines[y+1][x+1], lines[y+2][x+2]
        val4, val5 = lines[y+2][x], lines[y][x+2]
        
        # Check the pattern "MAS" with the swapped 'M' and 'S' in various forms
        if val1 == 'M' and val2 == 'A' and val3 == 'S':
            if (val4 == 'M' and val5 == 'S') or (val4 == 'S' and val5 == 'M'):
                p2 += 1
        
        # Check the swapped pattern with 'S' at the start
        val4, val5 = lines[y+2][x], lines[y][x+2]  # Reuse values to avoid redundant lookups
        if val1 == 'S' and val2 == 'A' and val3 == 'M':
            if (val4 == 'M' and val5 == 'S') or (val4 == 'S' and val5 == 'M'):
                p2 += 1

    return p2


def count_patterns(lines, sizeX, sizeY):
    p1 = 0
    p2 = 0
    
    for y in range(sizeY):
        for x in range(sizeX):
            p1 += check_p1_patterns(lines, y, x, sizeX, sizeY)
            p2 += check_p2_patterns(lines, y, x, sizeX, sizeY)

    return p1, p2




print(count_patterns(lines, len(lines[0]), len(lines)))