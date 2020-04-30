/**
 * @param {string[]} tokens
 * @return {number}
 * https://leetcode.com/problems/evaluate-reverse-polish-notation/
 */
var evalRPN = function(tokens) {
  return tokens.reduce((acc, curr) => {
    if (isNaN(curr)) {
      let last = Number(acc.pop());
      let secondToLast = Number(acc.pop());
      switch (curr) {
        case '*':
          acc.push(last * secondToLast);
          break;
        case '+':
          acc.push(last + secondToLast);
          break;
        case '/':
          acc.push(Math.trunc(secondToLast / last));
          break;
        case '-':
          acc.push(secondToLast - last);
          break;
      }
    } else acc.push(curr);
    return acc;
  }, [])[0];
};

// console.log(evalRPN(['2', '1', '+', '3', '*']));
// console.log(evalRPN(['4', '13', '5', '/', '+']));
// console.log(
//   evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
// );

// console.log(isNaN('*'));
// console.log('4' * '6');
// console.log(Math.trunc(6 / -132));
