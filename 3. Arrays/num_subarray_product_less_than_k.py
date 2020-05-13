class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        output = 0
        start = -1
        totalProduct = 1
        for idx in range(len(nums)):
            totalProduct *= nums[idx]
            while (start < idx and totalProduct >= k):
                start += 1
                totalProduct /= nums[start]

            output += idx - start
        return output
