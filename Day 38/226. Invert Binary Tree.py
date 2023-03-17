# Definition for a binary tree node.
# https://leetcode.com/problems/invert-binary-tree/submissions/917066304/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
            return root
