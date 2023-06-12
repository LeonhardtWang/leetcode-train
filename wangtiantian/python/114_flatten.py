# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if node is None:
                return None 

            left = helper(node.left)
            right = helper(node.right)
            
            node.left = None
            node.right = left
            if left is not None:
                while left.right is not None:
                    left = left.right 
                left.right = right
            else:
                node.right = right 
            
            return node 

        return helper(root)
