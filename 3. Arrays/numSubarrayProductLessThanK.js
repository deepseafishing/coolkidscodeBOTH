/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 713. Subarray Product Less Than K
 */
var numSubarrayProductLessThanK = function(nums, k) {
    if (k <= 1) return 0
    let start = -1;
    let output = 0;
    let totalProduct = 1;
    for (let i = 0; i < nums.length; i++) {
        totalProduct *= nums[i]
        while (start < i && totalProduct >= k) {
            start++;
            totalProduct /= nums[start]
        }
        output += i - start
    }

    return output
};

