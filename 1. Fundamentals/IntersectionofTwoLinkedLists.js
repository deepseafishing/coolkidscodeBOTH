const getIntersectionNode = (headA, headB) => {
  if (!headA || !headB) return null;
  let currA = headA;
  let currB = headB;

  while (currA !== currB) {
    currA = currA === null ? headB : currA.next;
    currB = currB === null ? headA : currB.next;
  }
  return currA;
};
