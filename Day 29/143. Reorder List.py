from typing import Optional
# https://leetcode.com/problems/reorder-list/submissions/916063046/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # Step 1: Find the middle point of the linked list.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the linked list into two halves.
        second_half = slow.next
        slow.next = None

        # Step 2: Reverse the second half of the linked list.
        prev, curr = None, second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        second_half = prev

        # Step 3: Merge the first half and the reversed second half alternately.
        curr1, curr2 = head, second_half
        while curr2:
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1, curr2 = next1, next2

        return head