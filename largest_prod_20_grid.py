grid = open('20_by_20_grid', 'r')

arry = []
for line in grid:
    arry.append(line)

for i in xrange(0,20):
    arry[i] = [int(x) for x in arry[i][0].split(' ')]

def walk(grid,num,col): # Hardcoded, bad but I know the rows are always 20 elmenents long
    if col + 4 <= len(grid[row]): #Walk horizontal and pick numbers
        yield list(nums[row][i] for i in xrange(col,col+4))#pick next four nos horizontally
    if row + 4 <= len(grid):
        yield list(nums[i][col] for i in xrange(row, row+4))
    if row + 4 <= len(grid) and col + 4 <= len(grid[row]):
        yield list(nums[row+i][col+i] for i in xrange(0,4)) #yield the 4 diagonal elements going to the right
    if row + 4 <= len(grid) and col >=3:
        yield list(nums[row+i][col-i] for i in xrange(0,4))#yield 4 diagnonal elements to the left

def walk_entire(arry):
    for row in xrange(0,len(arry)):
        for col in xrange(0,len(arry[row])):
            for sequence in walk(arry,row,col):
                yield sequence

def product(sequence):
    n = 1
    for no in sequence:
        n = n*no
    return n

print max(product(seq) for seq in walk_entire(arry))
