# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(p+q) = O(n) as we might need to iterate through all the trees
    # space complexity: O(n) in a degenerated tree but O(log n) in a balanced tree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # base case 
        if p == None and q == None:
                return True
        # both exist and are the same
        if p and q and p.val == q.val: 
            return (self.isSameTree(p.left,  q.left) and self.isSameTree(p.right,  q.right))

        # any other posibility
        return False
