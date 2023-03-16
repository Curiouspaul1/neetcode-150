# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/916092696/

from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0)
        dummy.next = head
        dic = {}
        curr = dummy


        while head:
            

            if head not in dic:
                dic[head] =  Node(head.val)
            curr.next = dic[head]

            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val)
            
                curr.next.random = dic[head.random]
            head = head.next
            curr = curr.next

        return dummy.next


