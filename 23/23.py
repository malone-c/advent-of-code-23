# increase max recursion depth
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_map = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

# Part 1
def hike():
    visited = set()
    def solve(i, j):
        if (i, j) in visited:
            return 0
        if (not 0 <= i < len(data)) or (not 0 <= j < len(data[0])):
            return 0
        if data[i][j] == '#':
            return 0
        if (i, j) == end:
            return 1
        
        visited.add((i, j))

        if data[i][j] in dir_map:
            di, dj = dir_map[data[i][j]]
            new = solve(i + di, j + dj)
        else:
            new = max(solve(i + di, j + dj) for di, dj in dirs)

        visited.remove((i, j))

        return 1 + new if new else 0
    return solve(*start) - 1

# Part 2
def find_junction_centres():
    junction_locs = set()
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if sum(data[i + di][j + dj] in dir_map for di, dj in dirs) >= 3:
                junction_locs.add((i, j))
    return junction_locs

def get_teleporter(junction_locs):
    teleporter = defaultdict(set)
    
    def dfs(i, j, path):
        if (
            (i, j) in path
            or (not 0 <= i < len(data)) 
            or (not 0 <= j < len(data[0]))
            or data[i][j] == '#'
        ):
            return 0, None
            
        if path and (i, j) in junction_locs | {start, end}:
            return 1, (i, j)

        for di, dj in dirs:
            n_steps, next_loc = dfs(i + di, j + dj, path | {(i, j),})
            if n_steps:
                return 1 + n_steps, next_loc

    for i, j in junction_locs:
        for di, dj in dirs:
            if data[i + di][j + dj] in dir_map:
                n_steps, next_loc = dfs(i + di, j + dj, path=set([(i, j)]))
                teleporter[(i, j)].add((n_steps, next_loc))
                teleporter[next_loc].add((n_steps, (i, j)))
        
    return teleporter

def hike2():
    junction_locs = find_junction_centres()
    teleporter = get_teleporter(junction_locs)
    visited = set()

    # TRAVERSE THE TELEPORTER
    def solve(i, j):
        if (i, j) in visited:
            return None
        if (i, j) == end:
            return 0
        visited.add((i, j))
        best = 0
        for n_steps, (ni, nj) in teleporter[(i, j)]:
            if (newsolve := solve(ni, nj)) is not None:
                best = max(best, n_steps + newsolve)
        visited.remove((i, j))

        return best if best else None
    
    return solve(*start)



with open('input.txt') as f:
    data = [[c for c in line.strip()] for line in f.readlines()]

for i in range(len(data[0])):
    if data[0][i] == '.':
        start = (0, i)
    if data[-1][i] == '.':
        end = (len(data) - 1, i)

print(hike())
print(hike2())
