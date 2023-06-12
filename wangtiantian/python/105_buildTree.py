# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: top, left, right
        # inorder: left, top, right
        def helper(preorder, inorder):
            if not preorder:
                return None
            top = preorder[0]
            root = TreeNode(top)

            for i, v in enumerate(inorder):
                if top == v:
                    break
            preorder_left = preorder[1:1+i]
            preorder_right = preorder[1+i:]

            inorder_left = inorder[:i]
            inorder_right = inorder[i+1:]
            left = helper(preorder_left, inorder_left)
            right = helper(preorder_right, inorder_right)
            root.left = left
            root.right = right
            return root
        return helper(preorder, inorder)


