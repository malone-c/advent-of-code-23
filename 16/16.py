# IMPORT RAM DEVOURER
import sys
sys.setrecursionlimit(10**8)


def lava(grid):

    def search(i, j, dir):
        if (i, j, dir) in visited:
            return
        
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return
        
        visited.add((i, j, dir))
        energised.add((i, j))

        if (grid[i][j] == '.'
            or (grid[i][j] == '|' and dir in 'ud')
            or (grid[i][j] == '-' and dir in 'lr')):
            # Keep moving in the same direction
            match dir:
                case 'r': j += 1
                case 'd': i += 1
                case 'l': j -= 1
                case 'u': i -= 1

            return search(i, j, dir)
        
        match grid[i][j]:
            case '|':
                search(i+1, j, 'd')
                search(i-1, j, 'u')
            case '-':
                search(i, j+1, 'r')
                search(i, j-1, 'l')
            case '/':
                match dir:
                    case 'l': i, dir = i+1, 'd'
                    case 'd': j, dir = j-1, 'l'
                    case 'r': i, dir = i-1, 'u'
                    case 'u': j, dir = j+1, 'r'
                search(i, j, dir)
            case '\\':
                match dir:
                    case 'l': i, dir = i-1, 'u'
                    case 'd': j, dir = j+1, 'r'
                    case 'r': i, dir = i+1, 'd'
                    case 'u': j, dir = j-1, 'l'
                search(i, j, dir)
            case _:
                print('Unrecognised character detected!')

    # Uncomment this for part 1
    # energised, visited = set(), set()
    # search(0, 0, 'r')
    # return len(energised)

    res = 0
    for r in range(len(data)):
        energised, visited = set(), set()
        search(r, 0, 'r')
        res = max(res, len(energised))

        energised, visited = set(), set()
        search(r, len(grid[0]) - 1, 'l')
        res = max(res, len(energised))

    for c in range(len(data[0])):
        energised, visited = set(), set()
        search(0, c, 'd')
        res = max(res, len(energised))

        energised, visited = set(), set()
        search(len(grid) - 1, c, 'u')
        res = max(res, len(energised))    

    return res



if __name__ == '__main__':
    with open('input.txt') as file:
        data = [[c for c in line] for line in file.read().splitlines()]

    print(lava(data))