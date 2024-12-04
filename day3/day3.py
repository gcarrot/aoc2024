import re

file = open('Day3/day3.txt').read().strip()

def extract_and_multiply(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, text)
    total_sum = 0
    for match in matches:
        x, y = int(match[0]), int(match[1])
        total_sum += x * y  
    
    return total_sum



def extract_and_multiply_with_conditions(text):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)
    total_sum = 0
    toggle = True
    for match in matches:
        if match == "do()":
            toggle = True
        elif match == "don't()":
            toggle = False
        else:
             if toggle:
                total_sum +=  extract_and_multiply(match)
    
    return total_sum


p1 = extract_and_multiply(file)
p2 = extract_and_multiply_with_conditions(file)

print(p1)
print(p2)