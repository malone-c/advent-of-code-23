import re

def scratchcards1(data):
    res = 0
    for targets, actuals in data:
        targets = set(int(n) for n in targets.split(' ') if n)
        actuals = set(int(n) for n in actuals.split(' ') if n)
        n_matches = len(targets & actuals)
        res += 2 ** (n_matches - 1) if n_matches else 0
    return res

def scratchcards2(data):
    n_copies = [1] * len(data)
    for i, (targets, actuals) in enumerate(data):
        targets = set(int(n) for n in targets.split(' ') if n)
        actuals = set(int(n) for n in actuals.split(' ') if n)
        n_matches = len(targets & actuals)
        for j in range(i + 1, i + 1 + n_matches):
            n_copies[j] += n_copies[i]
    return sum(n_copies)


if __name__ == '__main__':
    with open('input.txt') as lines:
        data = [re.sub('Card.*:', '', line.strip()).split('|') for line in lines]
    print(scratchcards1(data))
    print(scratchcards2(data))