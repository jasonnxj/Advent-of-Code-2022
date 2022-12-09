top_three = [0,0,0]
current = 0

with open('Aoc1/aoc1-input.txt') as f:
    calories = f.readlines()
    for cal in calories:
        cal = cal.strip()
        if cal != "":
            current += int(cal)
        else:
            top_three.sort()
            top_three[0] = max(top_three[0], current)
            current = 0
print(top_three)
print(sum(top_three))