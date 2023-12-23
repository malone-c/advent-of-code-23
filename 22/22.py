from collections import defaultdict, deque

minz_map = defaultdict(int)
supporters = defaultdict(set)
supportees = defaultdict(set)

def all_bricks_fall(cube, bricks):
    # Sort bricks by height
    bricks = sorted(bricks, key=lambda b: b[3][0])

    for name, xr, yr, zr in bricks:
        # Find the highest point under this brick
        highest = 0
        brick_height = zr[1] - zr[0] + 1
        for x in range(xr[0], xr[1] + 1):
            for y in range(yr[0], yr[1] + 1):
                if (nhigh := minz_map[(x, y)]) >= highest:
                    highest = nhigh

        # place the brick
        for x in range(xr[0], xr[1] + 1):
            for y in range(yr[0], yr[1] + 1):
                minz_map[(x, y)] = highest + brick_height
                for z in range(highest + 1, highest + 1 + brick_height):
                    cube[x][y][z] = name
                    if (supporter_name := cube[x][y][z-1]) not in [0, name]:
                        supportees[supporter_name].add(name)
                        supporters[name].add(supporter_name)

    count = 0
    for brick in bricks:
        name = brick[0]
        if name not in supportees:
            count += 1
            continue
        for supportee in supportees[name]:
            if len(supporters[supportee]) == 1:
                break
        else:
            count += 1
    print(count)

    def supports(a, b):
        return not supporters[b] - set(a)
    
    def solve(shifted):
        q = deque(shifted)
        while q:
            brick = q.popleft()
            for supportee in supportees[brick]:
                if supports(shifted, supportee):
                    shifted.add(supportee)
                    q.append(supportee)

        return len(shifted) - 1

    return sum(solve(set([brick[0]])) for brick in bricks)

                    
with open('input.txt') as f:
    lines = [line.strip().split('~') for line in f.readlines()]

lines = [[i+1, *[subline.split(',') for subline in line]] for i, line in enumerate(lines)]
bricks = [[line[0], *[[int(line[1][i]), int(line[2][i])] for i in range(3)]] for line in lines]

min_x = min(line[1][0] for line in bricks)
max_x = max(line[1][1] for line in bricks)
min_y = min(line[2][0] for line in bricks)
max_y = max(line[2][1] for line in bricks)
min_z = min(line[3][0] for line in bricks)
max_z = max(line[3][1] for line in bricks)

cube = [[[0 for _ in range(min_z, max_z+2)] for _ in range(min_y, max_y+1)] for _ in range(min_x, max_x+1)]

print(all_bricks_fall(cube, bricks))