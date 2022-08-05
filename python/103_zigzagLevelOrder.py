# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 双栈
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack_1 = [root]
        stack_2 = []
        record = 0
        while stack_1 or stack_2:
            if record % 2 == 0:
                tmp = []
                while stack_1:
                    node = stack_1.pop()
                    tmp.append(node.val)
                    if node.left:
                        stack_2.append(node.left)
                    if node.right:
                        stack_2.append(node.right)
            else:
                tmp = []
                while stack_2:
                    node = stack_2.pop()
                    tmp.append(node.val)
                    if node.right:
                        stack_1.append(node.right)
                    if node.left:
                        stack_1.append(node.left)
            res.append(tmp)
            record += 1
        return res
        