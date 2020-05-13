class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      maxLength, start = 0, 0
      map = {}
      for i in range(len(s)):
        if (s[i] in map):
          start = max(map[s[i]] + 1, start)
        map[s[i]] = i
        maxLength = max(maxLength, i - start + 1)
      return maxLength

