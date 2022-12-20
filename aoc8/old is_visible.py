def is_visible(row, column):
#check visibility in all 4 directions
    return (look_left(row, column) or look_right(row, column) or look_up(row, column) or look_down(row, column))

def look_left(row, column):
#check left visibility
    n = int(INPUT[row][column])              #current tree
    left = []
    for ind, i in enumerate(INPUT[row]):
        if ind < column:
            left.append(i)
    m = int(max(left, default=-1))
    if n > m:
        # print('Found: row=', row, 'col=', column, 'n=', n, 'm=', m,  'left=', left)
        return 1
    return 0

def look_right(row, column):
#check right visibility
    n = int(INPUT[row][column])              #current tree
    right = []
    for ind, i in enumerate(INPUT[row]):
        if ind > column:
            right.append(i)
    m = int(max(right, default=-1))
    if n > m:
        # print('Found: row=', row, 'col=', column, 'n=', n, 'm=', m,  'right=', right)
        return 1
    return 0

def look_up(row, column):
#check up visibility
    n = int(INPUT[row][column])
    up = []
    for ind, i in enumerate(INPUT):
        if ind < row:
            up.append(i[column])
    m = int(max(up, default=-1))
    if n > m:
        # print('Found: row=', row, 'col=', column, 'n=', n, 'm=', m,  'up=', up)
        return 1
    return 0

def look_down(row, column):
#check down visibility
    n = int(INPUT[row][column])
    down = []
    for ind, i in enumerate(INPUT):
        if ind > row:
            down.append(i[column])
    m = int(max(down, default=-1))
    if n > m:
        # print('Found: row=', row, 'col=', column, 'n=', n, 'm=', m,  'down=',down)
        return 1
    return 0