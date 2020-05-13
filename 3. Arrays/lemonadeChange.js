/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    let changes = {5: 0, 10: 0, 20: 0}
    for (let pay of bills) {
        if (pay === 5) {
            changes[pay] += 1;
        }
        else if (pay === 10){
            if (changes[5] == 0)
                return false
            changes[5] -= 1
            changes[10] += 1
        }
        else if (pay === 20) {
            if (changes[10] > 0 && changes[5] > 0){
                changes[10] -= 1
                changes[5] -= 1
            } else if (changes[5] > 2) {
                changes[5] -= 3;
            } else  {
                return false
            }
            changes[20] += 1
        }
    }
    return true
};
