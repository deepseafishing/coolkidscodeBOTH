def reverseLinkedList(head):

  curr = head
  prev = None
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev
