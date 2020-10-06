/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  const getEndIdx = (left) => {
    let lo = 0;
    let high = nums.length;
    while (lo < high) {
      let mid = Math.trunc((lo + high) / 2);
      if (nums[mid] > target || (nums[mid] === target && left)) {
        high = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  };

  if (!nums.length) return [-1, -1];
  let left = getEndIdx(true);

  if (left === nums.length || nums[left] !== target) return [-1, -1];

  return [left, getEndIdx(false) - 1];
};
