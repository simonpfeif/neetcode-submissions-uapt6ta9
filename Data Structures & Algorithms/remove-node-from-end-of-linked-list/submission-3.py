# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        dummy = ListNode(0, head)

        start = dummy
        end = dummy

        for _ in range(n):
            end = end.next

        while end.next:
            start = start.next
            end = end.next

        tmp = start.next
        start.next = start.next.next
        tmp = None

        return dummy.next
        
