def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
  right = head
  before = left = ListNode(-1)
  before.next = head
  while(right is not None and n != 0):
    n -= 1
    right = right.next
  while(right):
    right = right.next
    left = left.next
  left.next = left.next.next
  return before.next
