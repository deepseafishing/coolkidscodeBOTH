/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
   if (s.length !== t.length) return false;

   let charS = new Array(26).fill(0);
   let charT = new Array(26).fill(0);

   for (let i = 0; i < s.length; i++) {
       charS[s.charCodeAt(i) -97]++;
       charT[t.charCodeAt(i) -97]++;
   }

   for (let i = 0; i < 26; i++) {
       if (charS[i] !== charT[i]) {
           return false;
       }
   }

   return true;
};
