relations = [[1, 3], [2, 3]]
n = 3

# population  1... n
 # [a, b] -> a trusts b
 # town judge - everyone trusts this person, he trusts no one.
# answer = 3


# 1-> 3
#        <- 2

# indegree of town judge = n - 1
# outdegree of town judge = 0

# [[1, 2], [2, 3]]
# [0] * n => in
# [0] * n => out

def town_judge(relations, n):
  indegree = [0] * n
  outdegree = [0] * n
  for arr in relations:
    indegree[arr[1] - 1] += 1
    outdegree[arr[0] - 1] += 1
  ret =[]
  for i in range(0, n):
    if (indegree[i] == n - 1 and outdegree[i] == 0):
      ret.append(i + 1)

  return ret

print(town_judge(relations, 3))



# substring of length k, what's max number of vowels
s = "abciiidef"
k = 3
# abwer -> 3

# a, e, i, o, u

def max_vowels(s, k):
  vowels = {'a', 'e', 'i', 'o', 'u'}
  #vowels = Hashset('a','e', 'i', 'o', 'u')
  currLen = 0
  for i in range(0, k):
    if s[i] in vowels:
      currLen += 1
  maxLen = currLen
  for i in range(k, len(s)):
    if s[i] in vowels:
      currLen += 1
    if s[i - k] in vowels:
      currLen -= 1
    maxLen = max(maxLen, currLen)

  return maxLen

# print(max_vowels(s, k))

# s1 = "weallloveyou"

# print(max_vowels(s1, 7))





# custom range function
# write a function myrange(start, end) that returns a list of integers from start to end-1


# def myrange(start, end):
#     return [n for n  in range(start, end)]




# def myrange2(start, end):
#     output = []
#     while start < end:
#         output.append(start)
#         start += 1
#     return output


# #print(myrange2(3, 10))
# # print('hello')

# def myrangeGen(start, end):
#   while start < end:
#     yield start
#     start += 1

# myrangeGen(3, 10)
# getRowOfFile()

#   class Solution:
#     def expressiveWords(sc1, c2 in zip(count, count2))
# elf, S: str, words: List[str]) -> int:
#         def RLE(S):
#             return zip(*[(k, len(list(grp))) for k, grp in groupby(S)])
#         R, count = RLE(S)
#         ans = 0

#         for word in words:
#             R2, count2 = RLE(word)
#             if R2 != R:
#                 continue
#             ans += all(c1 >= max(c2, 3) or c1 ==
#                        c2 for
#         return ans
