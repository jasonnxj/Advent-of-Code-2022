def main():
    errors = []
    total = 0
    with open('input3.txt') as f:
        rucksack = f.readlines()
        for item in rucksack:
            item = item.strip()
            compsize = len(item)//2
            comp1 = item[:compsize]
            comp2 = item[compsize:]
            overlap = set(comp1) & set(comp2)
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
main()