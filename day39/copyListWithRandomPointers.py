"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from lib2to3.pytree import Node
from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyFromOriginal = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val) 
            copyFromOriginal[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = copyFromOriginal[curr]
            copy.next = copyFromOriginal[curr.next]
            copy.random = copyFromOriginal[curr.random]
            curr = curr.next

        return copyFromOriginal[head]