const isPalindrome = (head) => {
  let slow = head;
  let fast = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
  }

  let prev = null;
  while (slow) {
    let temp = slow.next;
    slow.next = prev;
    prev = slow;
    slow = temp;
  }

  while (prev) {
    if (prev.val !== head.val) return false;
    prev = prev.next;
    head = head.next;
  }
  return true;
};
