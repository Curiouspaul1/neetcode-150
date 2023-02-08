# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        values = set()

        while first and first.next :
            first = first.next
            val = first.val
            values.add(val)


            if first.val in values:
                return True

        return False