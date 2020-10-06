/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    let digits = Array(num1.length + num2.length).fill(0);
    let position = digits.length - 1;
    for (let i = num1.length - 1; i >= 0; i--) {
        tempPos = position;
        for (let j = num2.length - 1; j >= 0; j--) {
            digits[tempPos] += num1[i] * num2[j];
            digits[tempPos - 1] += Math.trunc(digits[tempPos] / 10);
            digits[tempPos] %= 10;
            tempPos -= 1;
        }
        position -= 1;
    }

    let zeroPaddingStartIdx = 0;
    while (zeroPaddingStartIdx < digits.length - 1 && digits[zeroPaddingStartIdx] === 0) {zeroPaddingStartIdx++;}
    return digits.slice(zeroPaddingStartIdx).join('');


};
