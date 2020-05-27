# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        before = ListNode(None, None)

        while head:
          prev = before
          print(prev)
          while prev.next and prev.next.val < head.val:
            prev = prev.next

          nextPivot = head.next
          head.next = prev.next
          prev.next = head
          head = nextPivot

        return before.next





