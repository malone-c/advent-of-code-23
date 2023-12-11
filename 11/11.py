from collections import deque
import math

# Determine length of shortest path between every
# pair of galaxies.
def cosmic(data, galaxies):
    res = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            # Compute shortest path
            (r1, c1), (r2, c2) = galaxies[i], galaxies[j]
            if r1 > r2:
                r1, r2 = r2, r1
            if c1 > c2:
                c1, c2 = c2, c1

            # (r1, c1) always to the top left of (r2, c2)
            count = 0
            while r1 < r2:
                count += data[r1][c1] if data[r1][c1] else 1
                r1 += 1
            while c1 < c2:
                count += data[r1][c1] if data[r1][c1] else 1
                c1 += 1

            res += count
    return res

if __name__ == '__main__':
    with open('input.txt') as file:
        data = [[int(c == '.') for c in line.strip()] for line in file.readlines()]
    galaxies = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == 0:
                galaxies.append((r, c))

    for row in data:
        if all(row):
            for i in range(len(row)):
                row[i] += 1_000_000 - 1
    for c in range(len(data[0])):
        if all([row[c] for row in data]):
            for row in data:
                row[c] += 1_000_000 - 1


    print(cosmic(data, galaxies))

# 9785747704315