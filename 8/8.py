
import re
import math

def walk(dirs, mapper, start_nodes):
    lcm = 1
    for node in start_nodes:
        n_steps = 0
        while node[2] != 'Z':
            node, n_steps = mapper[node][dirs[n_steps % len(dirs)]], n_steps + 1
        lcm = lcm * n_steps // math.gcd(lcm, n_steps)
    return lcm


if __name__ == '__main__':
    with open('input.txt') as file:
        dirs = [c == 'R' for c in file.readline().strip()]
        file.readline()

        lines = [re.sub('[^A-Z]', ' ', line).split() for line in file]

    mapper = {line[0]: (line[1], line[2]) for line in lines}

    # Part 1
    print(walk(dirs, mapper, ['AAA']))

    # Part 2
    print(walk(dirs, mapper, [line[0] for line in lines if line[0][2] == 'A']))