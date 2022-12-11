import re

l1 = ['H', 'C', 'R']
l2 = ['B', 'J', 'H', 'L', 'S', 'F']
l3 = ['R', 'M', 'D', 'H', 'J', 'T', 'Q']
l4 = ['S', 'G', 'R', 'H', 'Z', 'B', 'J']
l5 = ['R', 'P', 'F', 'Z', 'T', 'D', 'C', 'B']
l6 = ['T', 'H', 'C', 'G']
l7 = ['S', 'N', 'V', 'Z', 'B', 'P', 'W', 'L']
l8 = ['R', 'J', 'Q', 'G', 'C']
l9 = ['L', 'D', 'T', 'R', 'H', 'P', 'F', 'S']
L = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

def main():
    with open('input5.txt') as f:
        tasks = f.readlines()[10:]
        for x in tasks:
            x = x.strip()                                                       #remove \n
            x = list(map(int, re.findall('[0-9]+', x)))                         #extract list of 3 numbers
            x = {"quantity": x[0], "from": L[x[1]-1], "to": L[x[2]-1]}          #place into dict

            n = len(x["from"]) - x["quantity"]                                    #how many crates left after removing stack
            temp = x["from"][n:]
            x["to"].extend(temp)
            del x["from"][n:]
            
    s = ''
    for l in L:
        if len(l) > 0:
            s += l[-1]
    print(s, len(s))

main()
# x = [1,2,3,4,5,6,7,8,9]
# n = len(x) - 3
# temp = x[n:]
# del x[n:]
# print(x, temp)