/**
 * @param {string} S
 * @param {string[]} words
 * @return {number}
 */
var expressiveWords = function (S, words) {
  let ret = 0;

  function generateCounts(st) {
    let count = [];
    let alpha = [];

    for (let i = 0; i < st.length; i++) {
      if (alpha[alpha.length - 1] !== st[i]) {
        alpha.push(st[i]);
        count.push(1);
      } else {
        count[count.length - 1]++;
      }
    }
    return [count, alpha];
  }
  let [count, alpha] = generateCounts(S);

  for (let word of words) {
    let [wordCount, wordAlpha] = generateCounts(word);
    if (wordCount.length !== count.length) continue;

    let pass = false;

    for (let i = 0, j = 0; i < count.length && j < wordCount.length; i++, j++) {
      if (
        alpha[i] === wordAlpha[j] &&
        (count[i] === wordCount[j] ||
          (count[i] >= wordCount[j] && count[i] >= 3))
      ) {
        continue;
      } else {
        pass = true;
        break;
      }
    }
    if (!pass) ret++;
  }

  return ret;
};


function expressiveWords(S, words) {
    let count = 0;

    for (let w of words) {
      let i = 0; // tail of S
      let j = 0; // tail of w

      for (; i < S.length && j < w.length && w[j] === S[i];) {
        let lenS = 1;
        let lenW = 1;

        for (; i + lenS < S.length && S[i + lenS] === S[i]; lenS++);
        for (; j + lenW < w.length && w[j + lenW] === w[j]; lenW++);

        if (lenS < lenW || lenS > lenW && lenS < 3) break;

        i += lenS;
        j += lenW;
      }

      if (i === S.length && j === w.length) {
        count++;
      }
    }

    return count;
  }
