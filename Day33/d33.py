# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        previousNode = None

        if currentNode is None:
            return None
        
        while currentNode is not None:
            nextVal = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextVal

        return previousNode