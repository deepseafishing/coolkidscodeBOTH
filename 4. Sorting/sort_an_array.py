class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def helper (start, end):
            if start >= end:
                return
            i = start
            pivot = nums[end]
            for j in range(start, end):
                if nums[j] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i+= 1
            nums[end], nums[i] = nums[i], nums[end]
            helper(start, i - 1)
            helper(i + 1, end)

        helper(0, len(nums) - 1)

        return nums
