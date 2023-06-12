# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder: left, top, right
        # postorder: left, right, top
        def helper(inorder, postorder):
            if not inorder:
                return None
            
            top = postorder[-1]
            for i, v in enumerate(inorder):
                if top == v:
                    break

            inorder_left = inorder[:i]
            inorder_right = inorder[i+1:]
            postorder_left = postorder[:i]
            postorder_right = postorder[i:-1]
            left = helper(inorder_left, postorder_left)
            right = helper(inorder_right, postorder_right)

            root = TreeNode(top)
            root.left = left
            root.right = right
            return root 
        return helper(inorder, postorder)