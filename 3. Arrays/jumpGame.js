// Greedy
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let leftMost = nums.length - 1;
    for (let i = nums.length - 1; i >= 0; i--) {
        if (i + nums[i] >= leftMost) {
            leftMost = i;
        }
    }
    return leftMost === 0;
};


// Greedy
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let rightMost = 0;
    for (let idx = 0; idx < nums.length; idx++){
      let currJump = idx + nums[idx];
      if (idx > rightMost) return false;
      if (currJump > rightMost)
        rightMost =  currJump
    }
    return true
};
