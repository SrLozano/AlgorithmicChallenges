# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        
        # Ensure p has the smaller value
        if p.val > q.val:
            p, q = q, p

        while cur:
            # Case 1: Split point found — p <= cur <= q
            if p.val <= cur.val <= q.val:
                return cur
            
            # Case 2: Both nodes are smaller → go left
            elif cur.val > q.val:
                cur = cur.left
            
            # Case 3: Both nodes are larger → go right
            else:
                cur = cur.right
        
        return None
