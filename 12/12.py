from functools import cache

def foo(springs, counts):
    @cache
    def backtrack(i, j):
        if j == len(counts):
            return '#' not in springs[i:]
        
        if len(springs) - i < counts[j]:
            return 0
        
        if springs[i] == '.':
            return backtrack(i+1, j)

        if springs[i] == '#':
            if ('.' in springs[i: i + counts[j]]
                or (len(springs) - i > counts[j]
                    and springs[i + counts[j]] == '#')):
                return 0

            return backtrack(i + counts[j] + 1, j + 1)

        # springs[i] == '?'
        if ('.' in springs[i: i + counts[j]]
            or (len(springs) - i > counts[j]
                and springs[i + counts[j]] == '#')):
            return backtrack(i + 1, j)

        return backtrack(i + counts[j] + 1, j + 1) + backtrack(i + 1, j)
            
    return backtrack(0, 0)



if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.read().splitlines()
        data = [c.split(' ') for c in data]
        counts = [[int(n) for n in c[1].split(',')] * 5 for c in data]
        springs = [((c[0] + '?') * 5)[:-1] for c in data]

    print(sum(foo(springs[i], counts[i]) for i in range(len(springs))))