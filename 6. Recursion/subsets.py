# Approach 1: Cascading
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output
# Approach 2: Backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def _recursive_subsets(nums, i, arr):
            if i is len(nums):
                ret.append(arr)
            else:
                _recursive_subsets(nums, i + 1, arr + [nums[i]])
                _recursive_subsets(nums, i + 1, arr.copy())


        _recursive_subsets(nums, 0, [])

        return ret
# Approach 3: Bit operations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]

            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return output
