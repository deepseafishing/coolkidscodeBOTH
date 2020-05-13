/**
 * @param {number[]} A
 * @return {number}
 */
var longestMountain = function(A) {
    let maxLength = 0;
    if (!A.length) return 0;
    for (let i = 0; i < A.length;){
        let j = i;
        let up = false,
            down = false
        while(j < A.length - 1 && A[j] < A[j + 1]){
            j = j + 1
            up = true
        }
        let oldJ = j;
        while (j < A.length - 1 && A[j] > A[j + 1]) {
            j = j + 1
            down = true;
        }
        if (up && down)
        maxLength = Math.max(maxLength, j - i + 1);
        if ( i === j) {
            i++;
        } else {
            i = j;
        }
    }
    return maxLength;
};
