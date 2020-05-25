# def median(arr1, arr2):
#     totalLength = len(arr1) + len(arr2)
#     medianCount = totalLength // 2 + 1  # 4th one
#     i = 0 if len(arr1) // 2 - 1 < 0 else len(arr1) // 2 - 1
#     j = 0 if len(arr2) // 2 - 1 < 0 else len(arr2) // 2 - 1
#     step = 0

#     while(medianCount - 1 > i + j):
#         step = (medianCount - i - j) // 2
#         step1 = i + step
#         step2 = j + step

#         if ((arr1[i] if i < len(arr1) else float('inf')) > (arr2[j] if j < len(arr2) else float('inf'))):
#             j = step2
#         else:
#             i = step1

#     medianOne = arr2[j] if (arr1[i] if i < len(arr1) else float('inf')) > (arr2[j] if j < len(arr2) else float('inf')) else arr1[i]

#     if totalLength % 2 == 1:
#         return medianOne
#     else:
#         iBefore = float('-inf') if i -1 < 0 else arr1[i - 1]
#         jBefore = float('-inf') if j - 1 < 0 else arr2[j-1]
#         meidanBefore = arr1[i - 1] if iBefore > jBefore else arr2[j-1]
#         return (medianOne + meidanBefore) / 2

def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i > 0 and A[i - 1] > B[j]:
            imax = i - 1
        elif i < m and A[i] < B[j-1]:
            imin = i + 1
        else:
            if i == 0: max_left = B[j - 1]
            elif j == 0: max_left = A[i - 1]
            else: max_left = max(A[i-1], B[j- 1])

            if (m+n) % 2 == 1: return max_left

            if i == len(A): min_right = B[j]
            elif j == len(B): min_right = A[i]
            else: min_right = min(A[i], B[j])
            return (min_right + max_left) / 2



arr1 = [1, 2]
arr2 = [3, 4]
# median is (2 + 3) / 2 = 2.5
# arr1 = [1, 2, 3, 4, 5, 6]
# arr2 = [7]
# # # median = 4

arr1 = [1, 2, 3, 5, 6]
arr2 = [8, 9]

arr1 = [2]
arr2 = []

arr1 = []
arr2 = [2,3]
arr1 = [1]
arr2 = [2,3,4,5,6]
# print(median(arr1, arr2))
# # 7 numbers
# # 4th one
# # = > the index of the 3rd
