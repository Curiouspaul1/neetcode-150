# Definition for singly-linked list.

# https://leetcode.com/problems/add-two-numbers/submissions/916526723/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10
            sum_val = sum_val % 10

            current.next = ListNode(sum_val)
            current = current.next

        return dummy.next
