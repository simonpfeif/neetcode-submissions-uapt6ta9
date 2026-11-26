# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start2 = slow

        # step 2: reverse second half
        prev = None
        while start2:
            nxt = start2.next
            start2.next = prev
            prev = start2
            start2 = nxt
        start2 = prev # reset start to node
        start1 = head

        # step 3: build result
        while start1.next and start2.next:
            nxt1 = start1.next
            nxt2 = start2.next
            start1.next = start2
            start2.next = nxt1 

            start1 = nxt1 
            start2 = nxt2 
            print(start1.val, start2.val)

# [0, 1, 2, 3, 4, 5, 6]

# step 1: find middle
# [4, 5, 6]

# step 2: reverse second half
# [6, 5, 4]

# step 3: build result
# [0, 1, 2, 3]
# [6, 5, 4]
# = [0, 6, 1, 5, 2, 4, 3]

