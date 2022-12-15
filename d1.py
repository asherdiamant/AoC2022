

filename = "data/d1.txt"

with open(filename, "r") as data_file:
    data = data_file.readlines()

elves_food = []
curr_elf = 0
for line in data:
    if line == "\n":
        elves_food.append(curr_elf)
        curr_elf = 0
    else:
        curr_elf += int(line)

print("Part 1:", max(elves_food))

top3 = sorted(elves_food, reverse=True)[:3]
print("Part 2:", sum(top3))

