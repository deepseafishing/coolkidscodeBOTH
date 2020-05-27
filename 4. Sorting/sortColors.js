/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
  if (!nums.length) return [];
  let i = 0, j = nums.length - 1;
  let curr = 0;
  while (curr <= j) {
      if (nums[curr] === 0) {
          [nums[i], nums[curr]] = [nums[curr], nums[i]];
          i++;
          curr++;
      } else if (nums[curr] === 2) {
          [nums[j], nums[curr]] = [nums[curr], nums[j]];
          j--;
      } else if (nums[curr] === 1){
          curr++;
      }
  }
  return nums;
};
