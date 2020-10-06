/**
 * @param {string} s
 * @return {number}
 */
var countSubstrings = function(s) {
    let ret = 0;
    for (let i = 0; i < s.length; i++) {
        for (let j = 0; j < 2; j++) {
            let left = i;
            let right = i + j;
            while (left >= 0 && right < s.length && s[left] === s[right]) {
                ret++;
                left--;
                right++;
            }
        }
    }
    return ret;
};
