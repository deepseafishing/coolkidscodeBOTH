class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        for i, c in enumerate(s):
            for j in range(2):
                right = i + j
                left = i
                while left >= 0 and right < len(s) and s[right] == s[left]:
                    left -= 1
                    right += 1

                if right - left - 1 > len(ret):
                    ret = s[left + 1: right]

        return ret
