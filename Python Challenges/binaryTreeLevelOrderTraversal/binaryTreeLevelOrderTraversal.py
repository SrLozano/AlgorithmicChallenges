# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def descend_level(node, level):
            if node:
                # non necessary nonlocal when reassigning
                #nonlocal res
                res[level].append(node.val)
                descend_level(node.left, level+1)
                descend_level(node.right, level+1)
        
        descend_level(root, 0)

        return list(res.values())
