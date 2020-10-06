/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = strs => {
    const map = {};

    for (let str of strs) {
        const count = Array(26).fill(0);
        for (let ch of str){
            count[ch.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }
        const key = count.join('');

        if (!map[key]) {
            map[key] = [];
        }

        map[key].push(str);
    }

    return Object.values(map);
};

