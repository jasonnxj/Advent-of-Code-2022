def main():
    errors = []
    total = 0
    with open('Aoc3/input3.txt') as f:
        rucksack = f.readlines()
        rucksack = list(divide_chunks(rucksack, 3))
        for triples in rucksack:
            overlap = set(triples[0].strip()) & set(triples[1].strip()) & set(triples[2].strip())
            errors.extend(overlap)
    for item in errors:
        x = ord(item)
        #lowercase 65-90 >>>> 27-52
        if x >= 65 and x <= 90:
            total += x - 38
        #uppercase 97-122 >>>> 1-26
        elif x >= 97 and x <= 122:
            total += x - 96
        else:
            print("something's wrong lol")
    print(total)

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

main()