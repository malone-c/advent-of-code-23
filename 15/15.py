def lib(data):
    arr = [dict() for _ in range(256)]

    def transform(s):
        res = 0
        for c in s:
            res += ord(c) 
            res *= 17
            res %= 256
        return res
    
    for s in data:
        if '-' in s:
            label = s[:-1]            
            if label in arr[transform(label)]:
                del arr[transform(label)][label]
        else:
            label, num = s.split('=')
            arr[transform(label)][label] = int(num)

    # print(arr)
    res = 0
    for i in range(256):
        for j, v in enumerate(arr[i].values()):
            res += (i + 1) * (j + 1) * v
    return res

if __name__ == '__main__':
    with open('input.txt') as file:
        data = file.readline().split(',')
        # data = ['HASH']
    print(lib(data))



# 1. Get ASCII code
# 2. num += ascii
# 3. num *= 17
# 4. num %= 256