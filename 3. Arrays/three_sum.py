class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) < 3):
            return []
        ret = []
        nums.sort()
        for idx in range(len(nums) - 2):
            if (nums[idx] > 0):
                return ret
            if (idx == 0 or nums[idx] != nums[idx - 1]):
                i, j = idx + 1, len(nums) - 1
                while(i < j):
                    if (nums[idx] + nums[j] + nums[i] < 0 or (i > idx + 1 and nums[i - 1] == nums[i])):
                        i = i + 1
                    elif (nums[idx] + nums[j] + nums[i] > 0 or (j < len(nums) - 1 and nums[j + 1] == nums[j])):
                        j = j - 1
                    else:
                        # if they're equal
                        ret.append([nums[idx], nums[i], nums[j]])
                        i = i + 1
                        j = j - 1

        return ret
