/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let strArr = [...s.replace(/\W+/g, '').toLowerCase()];
    for (let i = 0, j = strArr.length - 1; i <= j; j--, i++)
        {
            if (strArr[i] !== strArr[j]) {return false;}
        }
    return true;
};
