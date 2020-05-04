# Input: [-15, -2, 2, -8, 7, 1]
# target sum: 0
# Output: 5

# 0: -15,
# 1: -17,
# 2: -15,
# 3: -23,
# 4: -16,
# 5: -15,

from typing import List


def get_max_sub_array(input: List[int], target: int) -> int:
    hash_map = {}
    sum = 0
    max_length = 0
    for idx, n in enumerate(input):
        sum += n
        if (sum in hash_map):
            max_length = idx - hash_map[sum] if idx - \
                hash_map[sum] > max_length else max_length
        else:
            hash_map[sum] = idx
    return max_length

print(get_max_sub_array([-15, -2, 2, -8, 7, 1], 0))
