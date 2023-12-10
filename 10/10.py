from collections import deque


def next_dir(grid, dir, r, c):
    # indir: which direction are we going in?
    if dir == 'right':
        if c < len(grid[0]) - 1 and grid[r][c] == '-':
            return (r, c+1)
        if r > 0 and grid[r][c] == 'J':
            return (r-1, c)
        if r < len(grid) - 1 and grid[r][c] == '7':
            return (r+1, c)
    if dir == 'left':
        if c > 0 and grid[r][c] == '-':
            return (r, c-1)
        if r < len(grid) - 1 and grid[r][c] == 'F':
            return (r+1, c)
        if r > 0 and grid[r][c] == 'L':
            return (r-1, c)
    if dir == 'down':
        if r < len(grid) - 1 and grid[r][c] == '|':
            return (r+1, c)
        if c > 0 and grid[r][c] == 'J':
            return (r, c-1)
        if c < len(grid[0]) - 1 and grid[r][c] == 'L':
            return (r, c+1)
    if dir == 'up':
        if r > 0 and grid[r][c] == '|':
            return (r-1, c)
        if c > 0 and grid[r][c] == '7':
            return (r, c-1)
        if c < len(grid[0]) - 1 and grid[r][c] == 'F':
            return (r, c+1)
        
    return False



# Generate directions to walk in
def dirs(r, c):
    return [(r+1, c, 'down'), 
            (r-1, c, 'up'), 
            (r, c+1, 'right'), 
            (r, c-1, 'left')]

# Update r, c
def walk(grid, start_r, start_c):
    visited.add((start_r, start_c))

    for r, c, dir in dirs(start_r, start_c):
        if (0 <= r < len(grid)
            and 0 <= c < len(grid[0])
            and (r, c) not in visited 
            and (temp := next_dir(grid, dir, r, c))
            and 0 <= temp[0] < len(grid)
            and 0 <= temp[1] < len(grid[0])):

            return (r, c)
        

def next_square(r, c):
    if grid[r][c] == 'J':
        return (r-1, c) if (r-1, c) not in visited else (r, c-1)
    if grid[r][c] == 'L':
        return (r-1, c) if (r-1, c) not in visited else (r, c+1)
    if grid[r][c] == '7':
        return (r+1, c) if (r+1, c) not in visited else (r, c-1)
    if grid[r][c] == 'F':
        return (r+1, c) if (r+1, c) not in visited else (r, c+1)
    if grid[r][c] == '-':
        return (r, c+1) if (r, c+1) not in visited else (r, c-1)
    if grid[r][c] == '|':
        return (r+1, c) if (r+1, c) not in visited else (r-1, c)


# Read data
with open('input.txt') as file:
    grid = [line.strip() for line in file.readlines()]

# Get start pos
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start_r = r
            start_c = c

visited = set([(start_r, start_c)])
l = []
for r, c, dir in dirs(start_r, start_c):
    if next_dir(grid, dir, r, c):
        l.append((r, c))


(r1, c1), (r2, c2) = l
count = 1
while (r1, c1) != (r2, c2):
    visited.update({(r1, c1), (r2, c2)})
    r1, c1 = next_square(r1, c1)
    r2, c2 = next_square(r2, c2)
    count += 1

visited.add((r1, c1))

print(count)



# ---------- PART 2 ----------

# J F L 7 | -

def is_interior(start_r, start_c):
    if (start_r, start_c) in visited:
        return False

    c = start_c
    r = count = 0
    while r < len(grid):
        if r == start_r and count % 2 == 0:
            # COUNT SHOULD BE ODD
            return False
        
        if (r, c) in visited:
            if grid[r][c] == '-':
                count += 1
            elif grid[r][c] == 'F':
                while r < len(grid):
                    if grid[r][c] in 'LJ':
                        count += grid[r][c] == 'J'
                        break
                    r += 1
            elif grid[r][c] == '7':
                while r < len(grid):    
                    if grid[r][c] in 'LJ':
                        count += grid[r][c] == 'L'
                        break
                    r += 1
        r += 1

    # COUNT SHOULD BE EVEN
    return count % 2 == 0
    

count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        count += is_interior(r, c)

print(count)