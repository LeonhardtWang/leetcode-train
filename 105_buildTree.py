# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        
        root_val = preorder[0]
        
        root = TreeNode(root_val)
        if len(preorder) == 1:
            return root
        for i, v in enumerate(inorder):
            if v == root_val:
                left_inorder = inorder[:i]
                right_inorder = inorder[i+1:]
                break
        left_preorder = preorder[1:i+1]
        right_preorder = preorder[i+1:]
        
        left_node = self.buildTree(left_preorder, left_inorder)
        right_node = self.buildTree(right_preorder, right_inorder)
        
        root.left = left_node
        root.right = right_node
        return root
        
        