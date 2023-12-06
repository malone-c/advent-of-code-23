import math
def seed1(seeds, maps):
    smallest_loc = math.inf
    for source in seeds:
        for seedmap in maps:
            dest = source
            for line in seedmap:
                if line[1] <= source < line[1] + line[2]:
                    dest = line[0] + (source - line[1]) # something like this...
            source = dest
        smallest_loc = min(smallest_loc, dest)
    return smallest_loc


def seed2(seed_pairs, maps):
    def solve(low, high, map_ind):
        newranges = []
        source_ranges = []
        for dest_start, source_start, range_size in maps[map_ind]:
            source_end = source_start + range_size
            dest_end = dest_start + range_size

            if high < source_start or low > source_end:
                continue
            
            if low <= source_start < high <= source_end: # Left overlap
                newranges.append((dest_start, dest_start + (high - source_start)))
                source_ranges.append((source_start, high))
            elif source_start <= low < source_end <= high: # right overlap
                newranges.append((dest_start + (low - source_start), dest_end))
                source_ranges.append((low, source_end))
            elif source_start < low < high < source_end: # centre
                newranges.append((dest_start + (low - source_start), dest_start + (high - source_start)))
                source_ranges.append((low, high))
            elif low < source_start < source_end < high: # wrapping
                newranges.append((dest_start, dest_end))
                source_ranges.append((source_start, source_end))

        if not newranges and map_ind < len(maps) - 1:
            return solve(low, high, map_ind + 1)
        elif not newranges:
            return low
        
        source_ranges.sort()
        if source_ranges[0][0] != low:
            newranges.append((low, source_ranges[0][0]))
        for i in range(len(source_ranges) - 1):
            if source_ranges[i][1] < source_ranges[i + 1][0]:
                newranges.append((source_ranges[i][1], source_ranges[i + 1][0]))
        if source_ranges[-1][1] != high:
            newranges.append((source_ranges[-1][1], high))

        if map_ind == len(maps) - 1:
            newranges.sort()
            return newranges[0][0]
        

        return min(solve(low, high, map_ind + 1) for low, high in newranges) if newranges else math.inf
        
    return min(solve(low, high, 0) if low < high else math.inf for low, high in seed_pairs)

if __name__ == '__main__':
    with open('input.txt') as file:
        file = [line.strip().split(' ') for line in file.readlines()]
        seeds = [int(n) for n in file[0][1:]]

        i = 3
        k = 0
        maps = [[]]
        while i < len(file):
            while i < len(file) and file[i][0].isnumeric():
                maps[k].append([int(n) for n in file[i]])
                i += 1
            else:
                i += 2
                k += 1
                maps.append([])
        maps.pop()
        

    print(seed1(seeds, maps))
    print(seed2([(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)], maps))

        # data = [line.strip() for line in file]