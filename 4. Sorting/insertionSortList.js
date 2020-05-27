function insertionSortList(head) {
  var before = { next: null };

  while (head) {
      var prev = before;

      // find prev
      while (prev.next && prev.next.val < head.val) {
          prev = prev.next;
      }

      var next = head.next;
      head.next = prev.next;
      prev.next = head;
      head = next;
  }

  return before.next;
}
