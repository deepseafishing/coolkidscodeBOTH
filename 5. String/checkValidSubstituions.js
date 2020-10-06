var isValid = function (S) {
    let stack = [];
    let valid = 'abc';
    for (let ch of S){
        stack.push(ch);
        if (ch === valid[valid.length - 1]){
            if (stack.length >= valid.length && valid === stack[stack.length - 3] + stack[stack.length - 2] + ch) {
            for (let i = 0; i < valid.length; i++) {
                    stack.pop();
                }
            } else {
                return false;
            }
    }
}
return !stack.length;
}
;
