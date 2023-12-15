from numpy import rot90

def rocks(data):
    # Get number of rocks in each column
    n_rocks = [0] * len(data[0])
    for j in range(len(data[0])):
        count = len(data)
        for i in range(len(data)):
            if data[i][j] == '#':
                count = len(data) - i - 1
                continue
            elif data[i][j] == 'O':
                n_rocks[j] += count
                count -= 1
    return sum(n_rocks)

def counter(data):
    count = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            count += (data[r][c] == 'O') * (len(data) - r)

    return count

def rockshifter(data):
    def shift():
        for c in range(len(data[0])):
            l = 0
            for r in range(len(data)):
                if data[r][c] == '#':
                    l = r + 1
                elif data[r][c] == 'O':
                    data[l][c], data[r][c] = data[r][c], data[l][c]
                    l += 1
                if l >= len(data):
                    break

    warmup = 200
    for i in range(warmup):
        for _ in range(4):
            shift()
            data = rot90(data, k=3)
    
    bignum = 1_000_000_000
    s = set()
    l = []

    while True:
        for _ in range(4):
            shift()
            data = rot90(data, k=3)

        tup = tuple(tuple(row) for row in data)
        if tup in s:
            break
        
        s.add(tup)
        l.append(counter(data))

    # warmup += len(l) + 1
    print(l)
    print((bignum - warmup))
    print(l[((bignum - warmup) % len(l)) - 1])

    # return counter(data)
                    
            

if __name__ == '__main__':
    with open('input.txt') as file:
        data = [[c for c in line] for line in file.read().splitlines()]

    print(rockshifter(data))
    # print(data)
    # print(rocks(data))

# 12816