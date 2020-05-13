
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        leftMost = len(nums) - 1
        for x in range(len(nums) - 1, -1, -1):
            # for x in range(len(nums)):
            # fromBack = -x - 1
            if (x + nums[x] >= leftMost):
                leftMost = x

        return leftMost == 0


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        rightMost = 0
        for idx in range(len(nums)):
            currJump = idx + nums[idx]
            if (idx > rightMost):
                return False
            if (currJump > rightMost):
                rightMost = currJump
        return True

