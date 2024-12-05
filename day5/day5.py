file = open('Day5/day5_small.txt').read().strip()
lines = file.split('\n')

def calc(values, mode):
    rules = []
    sum = 0
    for row in values:
        if "|" in row:
            rules.append(list(map(int, row.split("|"))))
        elif "," in row:
            row = list(map(int, row.split(",")))
            first = True
            while True:
                problems = []
                for a, b in rules:
                    if len(set([a, b]) & set(row)) == 2:
                        if row.index(a) > row.index(b):
                            problems.append((row.index(a), row.index(b)))
                            break
                
                if mode == 1:
                    if len(problems) == 0:
                        sum += row[(len(row) - 1) // 2 ]
                    break
                else:
                    if first and len(problems) == 0:
                        break
                    first = False
                    if len(problems) == 0:
                        sum += row[(len(row) - 1) // 2 ]
                        break
                    a, b = problems[0]
                    row[a], row[b] = row[b], row[a]

    return sum

print(calc(lines, 1))
print(calc(lines, 2))