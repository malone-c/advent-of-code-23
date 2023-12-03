def gears1():
    valid_locs = set()
    def surrounds(i, j):
        return [(a, b) for a in range(i-1, i+2) for b in range(j-1, j+2)]
    
    res = 0

    with open('input.txt') as lines:
        for i, line in enumerate(lines):
            line = line.strip()
            for j, c in enumerate(line):
                if c.isnumeric() or c == '.':
                    continue
                valid_locs.update(surrounds(i, j))
        
    with open('input.txt') as lines:
        for i, line in enumerate(lines):
            j = 0
            while j < len(line):
                flag = False
                newnum = []
                while j < len(line) and line[j].isnumeric():
                    if (i, j) in valid_locs:
                        flag = True
                    newnum.append(line[j]) 
                    j += 1
                if flag:
                    res += int(''.join(newnum))
                j += 1
    return res

                
def gears2():
    with open('input.txt') as lines:
        text = [line.strip() for line in lines]

    def search_num(i, j):
        visited = set([(i, j)])
        n_nums = 0
        res = 1
        for r in [i-1, i, i+1]:
            for c in [j-1, j, j+1]:
                if (r, c) in visited or not text[r][c].isnumeric():
                    continue
                newnum = []
                while c >= 1 and text[r][c-1].isnumeric():
                    c -= 1
                while c < len(text[0]) and text[r][c].isnumeric():
                    newnum.append(text[r][c])
                    visited.add((r, c))
                    c += 1

                n_nums += 1  
                res *= int(''.join(newnum))

                if n_nums > 2:
                    return 0

        return res if n_nums == 2 else 0
        
    res = 0
    for i, line in enumerate(text):
        for j, char in enumerate(line):
            if char == '*':
                res += search_num(i, j)
    
    return res


if __name__ == '__main__':
    print(gears1())
    print(gears2())

