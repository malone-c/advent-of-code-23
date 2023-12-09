import re
import math
from collections import Counter, defaultdict
from functools import reduce

# part 1
def read(num_lists):
    def solve(nums):
        diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
        if not any(nums):
            return nums[-1]
        return nums[-1] + solve(diffs)
    return sum(solve(nums) for nums in num_lists)

# part 2
def read(num_lists):
    def solve(nums):
        diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
        if not any(nums):
            return 0
        return nums[0] - solve(diffs)
    return sum(solve(nums) for nums in num_lists)


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = [[int(n) for n in line.split()] for line in file]

    print(read(lines))


# 2105967796
# Rigght answer 2105961943