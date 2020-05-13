def sign_alternating_array(arr):
  negIdx = 0
  posIdx = 0
  for i in range(len(arr)):
    if (i % 2 == 0):
      # this has to be negative
      if (arr[i] < 0):
        continue
      else:
        while(negIdx <= i or arr[negIdx] >= 0):
          negIdx += 1
          if (negIdx == len(arr)):
            return arr
        arr[i], arr[negIdx] = arr[negIdx], arr[i]
    else:
      # this has to be positive
      if (arr[i] >= 0):
        continue
      else:
        while(posIdx <= i or arr[posIdx] < 0):
          posIdx += 1
          if (posIdx == len(arr)):
            return arr
        arr[i], arr[posIdx] = arr[posIdx], arr[i]
  return arr

# input: [-1, 1, 2, -2, 3]
# Output: [-1, 1, -2, 2, 3]

# print(sign_alternating_array([-1, -1, 2, -2, 3, 5, 6, 7]))
print(sign_alternating_array([1, -1]))
# [-1, 1]

