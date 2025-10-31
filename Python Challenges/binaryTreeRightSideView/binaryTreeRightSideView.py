# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # time complexity: O(n) as we go through all the tree
    # space commplexity: O(n) as the worst case implies all elements in the list (degenerated tree) 
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_view = {}

        def dfs(node, level):
            if node:
                # if no right view for given level we add the elememt
                if level not in right_view.keys():
                    right_view[level] = node.val

                # prioritize right elements
                dfs(node.right, level+1)
                dfs(node.left, level+1)

        dfs(root, 0)
        return list(right_view.values())