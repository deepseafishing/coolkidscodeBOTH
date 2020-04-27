const removeNthFromEnd = (head, n) => {
  var right = head,
    left = head,
    before = head;
  left = before = { next: head };

  while (n--) right = right.next;
  while (right) {
    right = right.next;
    left = left.next;
  }
  left.next = left.next.next;

  return before.next;
};
