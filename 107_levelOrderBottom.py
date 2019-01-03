# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        curr_node_list = [root]
        res = []
        while curr_node_list:
            temp_res = []
            next_node_list = []
            for node in curr_node_list:
                temp_res.append(node.val)
                if node.left:
                    next_node_list.append(node.left)
                if node.right:
                    next_node_list.append(node.right)
            res.append(temp_res)
            curr_node_list = next_node_list
        return res[::-1]