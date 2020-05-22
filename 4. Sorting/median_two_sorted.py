def median(arr1, arr2):
    totalLength = len(arr1) + len(arr2)
    medianCount = totalLength // 2 + 1  # 4th one
    i = 0
    j = 0
    step = 0
    while(medianCount - 1 > i + j):
        step = (medianCount - i - j) // 2
        step1 = i + step
        step2 = j + step

        if ((arr1[i] if i < len(arr1) else float('inf')) > (arr2[j] if j < len(arr2) else float('inf'))):
            j = step2
        else:
            i = step1
        medianOne = arr2[j] if (arr1[i] if i < len(arr1) else float('inf')) > (
            arr2[j] if j < len(arr2) else float('inf')) else arr1[i]
        iBefore = arr1[i - 1] if i - \
            1 < len(arr1) and j - 1 >= 0 else float('inf')
        jBefore = arr2[j-1] if j - \
            1 < len(arr2) and i - 1 >= 0 else float('inf')
        meidanBefore = arr1[i - 1] if iBefore > jBefore else arr2[j-1]

    if totalLength % 2 == 1:
        return medianOne
    else:
        return (medianOne + meidanBefore) / 2


arr1 = [1, 2]
arr2 = [3, 4]
# median is (2 + 3) / 2 = 2.5
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [7]
# # # median = 4

arr1 = [1, 2, 3, 5, 6]
arr2 = [8, 9]
print(median(arr1, arr2))
# # 7 numbers
# # 4th one
# # = > the index of the 3rd
