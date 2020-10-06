# 10 7 3 5
# 15
# arr[i], arr[i+1]
'''
1 3 4 2 5
length of longest increasing subsequence
4
1 7 4 6

dp[i] = the length of longest increaing subseq up until that index i
ans = max (dp[i - 1] + 1 if the last value is less than the current one, dp[i-1] )

ans = dp[i-1] +  1 if arr[i] > arr[i-1]

dp[i] = max(dp[i], dp[j]+1) if arr[i] > arr[j] for 0 <= j < i
'''
def longest_sub(arr):
  dp = [0 for _ in range(len(arr))]
  for i in range(len(arr)):
    maxVal = 1
    for j in range(0, i):
      maxVal = max(maxVal, dp[j] + 1 if arr[i] > arr[j] else maxVal)

    dp[i] = maxVal

  return dp[len(arr) - 1]

print(longest_sub([1, 3, 4, 2, 5 ]))


'''
    take(i) -> arr[i] + soln(i-2)
    leave(i) -> soln(i-1)
    ans = max(take, leave)


def houseRobber(arr, i):
  if i < 0:
    return 0
  else:
    leave = houseRobber(arr, i-1)
    take = houseRobber(arr, i-2) + arr[i]
    ans = max(leave, take)
  return ans

t1 = [10, 7, 3, 5]
print(houseRobber(t1, len(t1)-1))

dp[i] = max loot ending at ith house
'''
# def houseRobberDP(arr):

#     dp = [0 for _ in range(len(arr))]

#     dp[0] = arr[0]
#     dp[1] = max(arr[0], arr[1])
#     for i in range(2, len(arr)):
#         dp[i] = max(dp[i-1], dp[i-2]+arr[i])
#     return max(dp)

# print(houseRobberDP([11, 12]))
# print(houseRobberDP([10, 7, 3, 5]))



# def getTreasure(arr):
#   def helper(start_idx, next_idx):
#     if next_idx >= len(arr)):
#       return 0
#     sum = 0
#     for j in range(start_idx + 2, len(arr)):


#     return


#   maxVal = 0
#   for i in range(len(arr)):
#     maxVal = max(maxVal, helper(i, i))



