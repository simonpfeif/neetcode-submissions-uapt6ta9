# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1 = first.next # 2
            tmp2 = second.next # 4

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


        # 1, 2, 3


        # 1, 2, 3, 4, 5
        # sp = 3
        # fp = 5

        # 1, 2, 3, 5, 4
        # mp = 3
        # start = 1

        # 1 -> 5 -> 2 -> 3 -> 5 -> 4
        # mp = 5
        # start = 3

        # 1 -> 5 -> 2 -> 4 -> 3 -> (5,4)

