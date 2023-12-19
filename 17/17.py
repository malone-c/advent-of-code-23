import sys
sys.setrecursionlimit(100000)
import heapq
import time
        

def dijkstra1(grid):
    
    # Dijkstra's algorithm
    q = [(0, 0, 0, (0, 1), 0), (0, 0, 0, (1, 0), 0)] # (count, i, j, dir, step_count)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    while q:
        count, i, j, dir, step_count = heapq.heappop(q)

        if (i, j, dir, step_count) in visited:
            continue
        visited.add((i, j, dir, step_count))

        if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
            return count

        for r, c in dirs:
            if not (0 <= i + r < len(grid) and 0 <= j + c < len(grid[0])): continue
            if (r, c) == (-dir[0], -dir[1]): continue

            newcount = count + grid[i + r][j + c]

            if (r, c) == dir and step_count < 3: 
                heapq.heappush(q, (newcount, i + r, j + c, (r, c), step_count + 1))
            elif (r, c) != dir:
                heapq.heappush(q, (newcount, i + r, j + c, (r, c), 1))  


def dijkstra2(grid):
    
    # Dijkstra's algorithm
    q = [(0, 0, 0, (0, 1), 0), (0, 0, 0, (1, 0), 0)] # (count, i, j, dir, step_count)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    while q:
        count, i, j, dir, step_count = heapq.heappop(q)

        if (i, j, dir, step_count) in visited:
            continue
        visited.add((i, j, dir, step_count))

        if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
            return count

        for r, c in dirs:
            if not (0 <= i + r < len(grid) and 0 <= j + c < len(grid[0])): continue
            if (r, c) == (-dir[0], -dir[1]): continue

            newcount = count + grid[i + r][j + c]

            if (r, c) == dir and step_count < 10: 
                heapq.heappush(q, (newcount, i + r, j + c, (r, c), step_count + 1))
            elif (r, c) != dir and 3 < step_count:
                heapq.heappush(q, (newcount, i + r, j + c, (r, c), 1))  



if __name__ == '__main__':
    with open('input.txt') as file:
        data = [[int(n) for n in line] for line in file.read().splitlines()]
    
    start_time = time.time()
    result = dijkstra1(data)
    end_time = time.time()
    
    print("Result:", result)
    print("Execution time:", end_time - start_time, "seconds")