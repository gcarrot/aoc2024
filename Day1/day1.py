from collections import  Counter
#infile = 'Day1/day1_small.txt'
infile = 'Day1/day1.txt'
file = open(infile).read().strip()

lines = file.split('\n')
LEFT = []
RIGHT = []
RC = Counter()

for line in lines:
    l,r = line.split()
    l,r = int(l),int(r)
    LEFT.append(l)
    RIGHT.append(r)
    RC[r] += 1
    
p1 = 0
LEFT = sorted(LEFT)
RIGHT = sorted(RIGHT)
for l,r in zip(LEFT,RIGHT):
    p1 += abs(r-l)
print(p1)

p2 = 0
for l in LEFT:
    p2 += l * RC.get(l,0)
print(p2)

p3 = 0
for l in LEFT:
    p3 += l * RIGHT.count(l)
print(p3)