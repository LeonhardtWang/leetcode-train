# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.record = 0 # 记得该节点前面节点的总和
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        self.convertBST(root.right)
        root.val += self.record
        self.record = root.val
        self.convertBST(root.left)
        return root
        