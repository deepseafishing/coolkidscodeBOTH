class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)
        start = -1
        end = -1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                while mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                    mid -= 1
                start = mid
                while mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    mid += 1
                end = mid
                return [start, end]
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return [start, end]



class Solution:
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            print(lo, hi)
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)
        print(left_idx)
        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
