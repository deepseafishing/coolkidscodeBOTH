// const ladderLength = function(beginWord, endWord, wordList) {
//     if (!wordList.includes(endWord)) return false;
//     let reached = [beginWord],
//       distance = 1;
//     while (!reached.includes(endWord)) {
//       let tmpArr = [];
//       for (let each of reached) {
//         for (let i = 0; i < each.length; i++) {
//           let curArr = each.split('');
//           for (let k = 'a'.charCodeAt(0); k <= 'z'.charCodeAt(0); k++) {
//             curArr[i] = String.fromCharCode(k);
//             let tem = curArr.join('');
//             if (wordList.includes(tem)) {
//               tmpArr.push(tem);
//               wordList.splice(wordList.indexOf(tem), 1);
//             }
//           }
//         }
//       }
//       distance++;
//       if (!tmpArr.length) return 0;
//       reached = tmpArr;
//     }
//     return distance;
//   };

  const ladderLength = function(beginWord, endWord, wordList) {
    if (!wordList.includes(endWord)) return false;
    let reached = [beginWord],
      distance = 1;
    let interMap = {};
    for (let word of wordList){
        for (let i = 0; i < word.length; i++) {
             word[i] = '*';
             interMap[word] ? interMap[word].push(word) : interMap[word] = [];
        }
    }

      while (!reached.includes(endWord)) {
      let tmpArr = [];
      for (let each of reached) {
        for (let i = 0; i < each.length; i++) {
          each[i] = '*'
          for (let word of interMap[each]){
            if (word === endWord) return distance + 1

          }
        }
    }
      }
      distance++;
      if (!tmpArr.length) return 0;
      reached = tmpArr;
    }
    return distance;
  };
