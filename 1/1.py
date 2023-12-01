from collections import defaultdict

def trebuchet1():
    res = 0
    with open('input.txt') as input:
        for line in input:
            for c in line:
                if c.isnumeric():
                    new = 10 * int(c)
                    break

            for c in reversed(line):
                if c.isnumeric():
                    new += int(c)
                    break
            res += new
    return res

def trebuchet2():
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    word_map = {words[i][0:2]: words[i] for i in range(10)}
    num_map = {words[i]: i for i in range(10)}

    def word_check(i):
        if (
            i <= len(line) - 2 and
            (chars := line[i:i+2]) in word_map and 
            i <= len(line) - len(word_map[chars]) and
            (word := line[i:i+len(word_map[chars])]) == word_map[chars]
        ):
            return num_map[word]
        
        return 0

    
    res = 0
    with open('input.txt') as input:
        for line in input:
            for i, c in enumerate(line):
                if c.isnumeric():
                    new = 10 * int(c)
                    break
                if (num := word_check(i)):
                    new = 10 * num
                    break

            for i in reversed(range(len(line))):
                c = line[i]
                if c.isnumeric():
                    new += int(c)
                    break
                if (num := word_check(i)):
                    new += num
                    break
                    
            res += new
    return res



if __name__ == '__main__':
    print(trebuchet1())
    print(trebuchet2())