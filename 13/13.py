def mirror(data):
    count = 0
    for i in range(len(data) - 1):
        l, r = i, i + 1
        while l >= 0 and r < len(data):
            if data[r] != data[l]:
                break
            l -= 1
            r += 1
        else:
            count += 100 * (i + 1)

    for j in range(len(data[0]) - 1):
        l, r = j, j + 1
        while l >= 0 and r < len(data[0]):
            if [row[l] for row in data] != [row[r] for row in data]:
                break
            l -= 1
            r += 1
        else:
            count += (j + 1)

    return count


def mirror(data):
    count = 0
    for i in range(len(data) - 1):
        l, r = i, i + 1
        smudges_allowed = 1
        while l >= 0 and r < len(data):
            n_matches = sum(data[r][j] == data[l][j] for j in range(len(data[0])))

            if n_matches == len(data[0]) - 1:
                if smudges_allowed == 0:
                    break
                smudges_allowed -= 1
            elif n_matches != len(data[0]):
                break
            l -= 1
            r += 1
        else:
            if smudges_allowed == 0:
                count += 100 * (i + 1)

    for j in range(len(data[0]) - 1):
        l, r = j, j + 1
        smudges_allowed = 1
        while l >= 0 and r < len(data[0]):
            n_matches = sum(data[i][r] == data[i][l] for i in range(len(data)))
            if n_matches == len(data) - 1:
                if smudges_allowed == 0:
                    break
                smudges_allowed -= 1
            elif n_matches != len(data):
                break
            l -= 1
            r += 1
        else:
            if smudges_allowed == 0:
                count += (j + 1)

    return count

            
            
            
            

if __name__ == '__main__':
    with open('input.txt') as file:
        # data = file.read().splitlines()
        squares = [line.split('\n') for line in file.read().split('\n\n')]

    # print(mirror(squares[0]))
    print(sum(mirror(square) for square in squares))