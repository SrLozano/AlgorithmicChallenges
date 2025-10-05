# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        if root: 
            dq.append((root, 1))
            
        max_depth = 0
        while len(dq) > 0:
            element, depth = dq.popleft()
            max_depth = max(max_depth, depth) 
            if element.left:
                dq.append((element.left, depth + 1))
            if element.right:
                dq.append((element.right, depth + 1))
        
        return max_depth