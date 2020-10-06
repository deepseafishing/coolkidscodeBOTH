'''
1 2 6
0 3 3
7 8 9

What's the maximum amount of points that can be collected in the path
from (0, 0) to bottom right corner? Can travel only right or down in each step.
1+0+7+8+9
'''

def maxCollect(grid):
  mem = [0 for _ in range(len(grid[0]))]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if j - 1 >= 0:
        mem[j] = max(mem[j - 1], mem[j]) + grid[i][j]
      else:
        mem[j] = mem[j] + grid[i][j]
  return mem[len(mem) - 1]
        
m = [[1, 2, 6],
     [0, 3, 3],
     [7, 8, 9]]

print(maxCollect(m))



'''
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a
 list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).



Example 1:

Input: [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.

Input: [9,4,7,2,10]
Output: 3
Explanation:
The longest arithmetic subsequence is [4,7,10].


'''

from collections import defaultdict
def LAS(arr):
  dp = defaultdict(dict)
  max_len = 2
  for i in range(len(arr)):
    for j in range(i):
      diff = arr[i]-arr[j]
      # add 1 to previous LAS ending at j
      dp[i][diff] = dp[j].get(diff, 1) + 1
      max_len = max(max_len, dp[i][diff])
  
  return max_len
    

a = [3, 6, 9, 12]
print(LAS(a))
'''
1 + dp[j][3]

Input: [9,4,7,2,10]
DP[2:{-2:2, 3:2}, 4:{3:3}]
dp[i][D] = length of LAS arr[0...i] of difference D

'''
