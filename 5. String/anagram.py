class Solution:
  def isAnagram(self, s, t):
    if len(s) != len(t): return False
    counts = [0] * 26
    for c1, c2 in zip(s,t):
      counts[ord(c1) - ord('a')] += 1
      counts[ord(c2) - ord('a')] -= 1

    for n in counts:
      if n != 0: return False
    return True
