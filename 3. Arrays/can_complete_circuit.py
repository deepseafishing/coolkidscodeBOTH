# https://leetcode.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalSum, currSum, start = 0, 0, 0
        for idx, (gi, ci) in enumerate(zip(gas, cost)):
            totalSum += gi - ci
            currSum += gi - ci
            if currSum <0:
                start = idx + 1
                currSum = 0

        if totalSum >= 0:
            return start
        return -1
