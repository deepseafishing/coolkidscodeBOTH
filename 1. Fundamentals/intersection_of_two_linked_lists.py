class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    currA = headA
    currB = headB
    while(currA is not currB):
      currA = currA.next if currA is not None else headB
      currB = currB.next if currB is not None else headA

    return currA
