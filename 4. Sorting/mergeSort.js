/**
 * @param {number[]} nums
 * @return {number[]}
 */
const sortArray = nums => {
  mergeSort(nums, 0, nums.length - 1);
  return nums;
};

const mergeSort = (nums, left, right) => {
  if (left >= right) return;

  const mid = Math.floor((right - left) / 2) + left;
  mergeSort(nums, left, mid);
  mergeSort(nums, mid + 1, right);
  merge(nums, left, mid, mid + 1, right);
};

const merge = (nums, leftStart, leftEnd, rightStart, rightEnd) => {
  const sorted = [...nums];
    let i = leftStart;
  while (leftStart <= leftEnd || rightStart <= rightEnd) {
    if (
      (leftStart <= leftEnd && sorted[leftStart] <= sorted[rightStart]) ||
      rightStart > rightEnd
    ) {
      nums[i] = sorted[leftStart];
      leftStart += 1;
    } else {
      nums[i] = sorted[rightStart];
      rightStart += 1;
    }
    i += 1;
  }
};
