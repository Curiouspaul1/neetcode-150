# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle/submissions/916528100/

class Solution:
    def hasCycle(self, head ) -> bool:
        hash_dic = dict()
        
        while head:
            if head in hash_dic:
                return True
            else:
                hash_dic[head] = head
            
            head = head.next
        return False
        
#         slow, fast = head, head        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#             if fast == slow:
#                 return True
#         return False