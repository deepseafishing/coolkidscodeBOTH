class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key=lambda x: (x[0], x[1]))
        prev = intervals[0]
        ret = [prev]
        for curr in intervals:
            if prev[1] >= curr[0]:
                prev[1] = max(curr[1], prev[1])
            else:
                ret.append(curr)
                prev = curr

        return ret
