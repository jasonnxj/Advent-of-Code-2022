biggest = 0
current = 0

with open('Aoc1/aoc1-input.txt') as f:
    calories = f.readlines()
    for cal in calories:
        cal = cal.strip()
        if cal != "":
            current += int(cal)
        else:
            biggest = max(biggest, current)
            current = 0
print(biggest)