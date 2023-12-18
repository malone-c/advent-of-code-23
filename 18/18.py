from collections import defaultdict
import time

dir2tup = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

def lagoon(data):
    r = c = boundary = interior = 0
    for dir, steps in data:
        dr, dc = dir2tup[dir]
        boundary += steps
        interior -= r * (c + steps * dc) - (r + steps * dr) * c
        r, c = r + steps * dr, c + steps * dc

    return  (boundary // 2) + 1 + interior // 2


int2dir = {
    '0': 'R', 
    '1': 'D', 
    '2': 'L', 
    '3': 'U'
}

with open('input.txt') as file:
    data = [line.replace('(', '').replace(')', '').replace('#', '').split(' ') for line in file.read().splitlines()]
    # print(data)
    
    # Part 1
    # data = [[line[0], int(line[1])] for line in data]

    # Part 2
    data = [[int2dir[line[2][-1]], int(line[2][:5], 16)] for line in data]
    
start_time = time.time()
result = lagoon(data)
end_time = time.time()

print("Result:", result)
print("Execution time:", end_time - start_time, "seconds")