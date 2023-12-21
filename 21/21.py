from functools import cache

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def n_locs(n_steps):
    locs = {start,}
    locsnew = set()

    for _ in range(n_steps):
        for loc in locs:
            for loc in get_next_steps(*loc):
                locsnew.add(loc)

        locs = locsnew.copy()
        locsnew = set()

    return len(locs)

with open('input.txt') as f:
    lines = [[c for c in line.strip()] for line in f.readlines()]

for i, row in enumerate(lines):
    for j, c in enumerate(row):
        if c == 'S':
            start = (i, j, 0, 0)

@cache
def get_next_steps(i, j, square_i, square_j):
    out = set()

    if i == 0:
        if lines[-1][j] != '#':
            out.add((len(lines) - 1, j, square_i - 1, square_j))
    elif lines[i - 1][j] != '#':
        out.add((i - 1, j, square_i, square_j))

    if i == len(lines) - 1:
        if lines[0][j] != '#':
            out.add((0, j, square_i + 1, square_j))
    elif lines[i + 1][j] != '#':
        out.add((i + 1, j, square_i, square_j))

    if j == 0:
        if lines[i][-1] != '#':
            out.add((i, len(lines[0]) - 1, square_i, square_j - 1))
    elif lines[i][j - 1] != '#':
        out.add((i, j - 1, square_i, square_j))

    if j == len(lines[0]) - 1:
        if lines[i][0] != '#':
            out.add((i, 0, square_i, square_j + 1))
    elif lines[i][j + 1] != '#':
        out.add((i, j + 1, square_i, square_j))

    return out

m = len(lines)
goal = 26501365
startgap = goal % m

def f(n):
    x = n_locs(startgap)
    y = n_locs(startgap + m)
    z = n_locs(startgap + 2*m)

    
    a = 1/2 * (-2 * x + y + z) 
    b = 1/2 * (4 * x - y - 3 * z)
    c = z

    return int(a * n**2 + b * n + c)

print(f(goal//m))