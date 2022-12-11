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

with open('input5.txt') as f:
    tasks = f.readlines()[10:]
    for x in tasks:
        x = x.strip()                                                       #remove \n
        x = list(map(int, re.findall('[0-9]+', x)))                         #extract list of 3 numbers
        x = {"quantity": x[0], "from": L[x[1]-1], "to": L[x[2]-1]}                    #place into dict
                                                    
        for i in range(x["quantity"]):                                      #loop over quantity
            x["to"].append(x["from"][-1])
            x["from"].pop(-1)
            
s = ''
for l in L:
    if len(l) > 0:
        s += l[-1]
print(s)