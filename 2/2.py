import re
from math import prod
from collections import defaultdict

d = {'r': 12, 'g': 13, 'b': 14}

def cube1():
    res = 0
    with open('./input.txt') as lines:
        for i, line in enumerate(lines):
            game = [x.split(' ') for x in re.sub('Game.*?: ', '', line).replace(';', ',').split(', ')]
            for n, colour in game:
                if d[colour[0]] < int(n):
                    break
            else:
                res += i + 1

    return res

def cube2():
    res = 0
    with open('input.txt') as lines:
        for i, line in enumerate(lines):
            game = [x.split(' ') for x in re.sub('Game.*?: ', '', line).replace(';', ',').split(', ')]
            max_dict = defaultdict(int)
            for n, colour in game:
                max_dict[colour[0]] = max(max_dict[colour[0]], int(n))
            res += prod(max_dict[n] for n in d.keys())
    return res

if __name__ == '__main__':
    print(cube1())
    print(cube2())