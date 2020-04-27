const isValid = function(s) {
    let open = {},
        close = {};
    [
        ['(', ')'],
        ['{', '}'],
        ['[', ']'],
    ].forEach(([o, c]) => {
        open[o] = c;
        close[c] = o;
    });

    console.log(open, close);

    let stack = [];
    for (let i = 0; i < s.length; i++) {
        if (open.hasOwnProperty(s[i])) {
            stack.push(s[i]);
        } else if (close.hasOwnProperty(s[i])) {
            if (open[stack.pop()] !== s[i]) return false;
        }
    }

    return stack.length === 0;
};
