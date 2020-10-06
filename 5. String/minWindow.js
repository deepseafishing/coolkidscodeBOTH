/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  // preprocess t
  let map = new Map();
  let ans = '';
  for (let c of t) {
    map[c] = (map[c] || 0) + 1;
  }
  let count = Object.keys(map).length;
  // we will decrease count when it matches
 
  for (let left = 0, right = -1; right < s.length; ) {
    if (count === 0) {
      if (!ans || ans.length > right - left + 1) {
        ans = s.substring(left, right + 1);
      }

      if (map[s[left]] !== undefined) {
        map[s[left]]++;
        if (map[s[left]] > 0) count++;
      }
      left++;
    } else {
      right++;
      if (map[s[right]] !== undefined) {
        map[s[right]]--;
        if (map[s[right]] === 0) count--;
      }
    }
  }
  return ans;
};

// /**
//  * @param {string} s
//  * @param {string} t
//  * @return {string}
//  */
// var minWindow = function(s, t) {
//     // preprocess t

//     let set = new Set(t)
//     let map = new Map();
//     let minLen = Number.MAX_SAFE_INTEGER;
//     let minLeft = 0;
//     let minRight = 0;
//     for (let left = -1, right = -1; right < s.length; ) {
//         console.log('left', s[left], 'right', s[right])
//         console.log(map)
//         if (Object.keys(map).length === set.size) {
//             if (minLen > right - left + 1){
//                 minLen = right - left + 1
//                 minLeft = left
//                 minRight = right
//             }

//             if (set.has(s[left])){
//                 map[s[left]]--
//                 if (map[s[left]] === 0) {
//                     delete map[s[left]]
//                 }
//             }
//             left++;

//         } else {
//             right++
//             if (set.has(s[right])){
//                 map[s[right]] = (map[s[right]] || 0) + 1
//             }
//         }
//     }
//     return s.substring(minLeft, minRight + 1);
// };
