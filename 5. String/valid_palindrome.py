class Solution:
    def isPalindrome(self, s):
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        if len(new_s) == 0:
            return True
            # start = 0
        # end = len(new_s) - 1

        # while start < end:
        #     if new_s[start] != new_s[end]:
        #         return False
        #     start += 1
        #     end -= 1
        # return True
        if len(new_s) % 2:
            lo = len(new_s) // 2 - 1
            hi = len(new_s) // 2 + 1
        else:
            lo, hi = len(new_s) // 2 - 1, len(new_s) // 2
            if new_s[lo] != new_s[hi]:
                return False
            lo -= 1
            hi += 1

        while (lo >= 0 and hi < len(new_s)):
            if new_s[lo] != new_s[hi]:
                return False
            lo -= 1
            hi += 1

        return True
