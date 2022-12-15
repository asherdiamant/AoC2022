filename = "data/d2.txt"

with open(filename, "r") as data_file:
    data = data_file.readlines()

part1_strat = {
    ('A', 'X'): 4,
    ('A', 'Y'): 8,
    ('A', 'Z'): 3,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 7,
    ('C', 'Y'): 2,
    ('C', 'Z'): 6,
}

part2_strat = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7,
}

part1_score = 0
part2_score = 0
for line in data:
     # print(line)
    opp, me = line.strip().split(" ")
    part1_score += part1_strat[(opp, me)]
    part2_score += part2_strat[(opp, me)]

print("Part 1:", part1_score)
print("Part 2:", part2_score)