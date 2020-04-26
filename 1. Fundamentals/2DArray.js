let N = 3;
// This will Not work because the list is pass by reference. Each element will refer to the same list.
let wrongArray = Array(N).fill(Array(N).fill(0));
wrongArray[0][1] = 1;
console.log(wrongArray);

let rightArray = Array(N)
  .fill(0)
  .map((x) => Array(N).fill(0));
rightArray[0][1] = 1;
console.log(rightArray);
