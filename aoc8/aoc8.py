INPUT = []
ROWS = 0
COLUMNS = 0

def main():
    with open('aoc8/input8.txt') as f:
    #populate input
        input = f.readlines()
        for text in input:
            text = text.strip()
            INPUT.append(text)                                      #debug rows and columns
    ROWS = len(INPUT)
    COLUMNS = len(INPUT[0])
    print('== POPULATE INPUT SUCCESSFUL ===============================================================================================================================================================')
    print('ROWS =', ROWS, 'COLUMNS =', COLUMNS)

    print('== CHECKING VISIBILITY ===============================================================================================================================================================')
    count = 0
    score = 0
    for row, x in enumerate(INPUT):
        for col, y in enumerate(x):
            count += is_visible(row, col)
            score = max(score, scenic_score(row, col))
    print('Part 1: Number of visibles: ', count)
    print('Part 2: Scenic score: ', score)



def is_visible(row, column):
#check visibility in all 4 directions
    n = int(INPUT[row][column])              #current tree
    left, right, up, down = [], [], [], []
    trees = [left, right, up, down]

    #left
    for ind, i in enumerate(INPUT[row]):
        if ind < column:
            left.append(i)

    #right
    for ind, i in enumerate(INPUT[row]):
        if ind > column:
            right.append(i)

    #up
    for ind, i in enumerate(INPUT):
        if ind < row:
            up.append(i[column])

    #down
    for ind, i in enumerate(INPUT):
        if ind > row:
            down.append(i[column])
    default=-1
    #check
    for direction in trees:
        m = int(max(direction, default=-1))
        # print(n, row, column)
        if n > m:
            return 1
    return 0

def scenic_score(row, column):
    n = int(INPUT[row][column])              #current tree
    left = up = right = down = 0

    #left
    for i in reversed(INPUT[row][0:column]):
        left += 1
        if int(i) >= n:
            break

    #right
    for i in INPUT[row][column+1:]:
        right += 1
        if int(i) >= n:
            break

    #up
    for i in reversed(INPUT[:row]):
        up += 1
        if int(i[column]) >= n:
            break
            
    #down
    for i in INPUT[row+1:]:
        down += 1
        if int(i[column]) >= n:
            break
    
    print(row, column, n, '-----> left =', left, 'right =', right, 'up =', up, 'down =', down, '-----> score=', left*right*up*down)
    return left*right*up*down

main()
a = ['foo', 'bar', 'baz', 'paul']
# for i, e in reversed(list(enumerate(a[2:]))):
# for i, e in enumerate(INPUT[2:]):
#     print(i, e)
# row = 2
# column = 1
# for i in INPUT[:row]:
#     print(i[column])
print('== END ===============================================================================================================================================================')