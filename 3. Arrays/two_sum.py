class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            another = target - nums[i]
            if (another in map):
                return [map[another], i]
            map[nums[i]] = i
