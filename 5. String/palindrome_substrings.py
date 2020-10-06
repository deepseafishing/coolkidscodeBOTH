class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for i, c in enumerate(s):
            for j in range(2):
                right = i + j
                left = i
                while left >= 0 and right < len(s) and s[right] == s[left]:
                    ret += 1
                    left -= 1
                    right += 1

        return ret
