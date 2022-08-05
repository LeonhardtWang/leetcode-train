# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self._helper(root))
    
    def _helper(self, root):
        # 每个节点只有选和不选两种状态
        # 分别保存以当前节点为根节点两种状态下的最高金额
        res = [0, 0] # 索引0表示不选，索引1表示选
        if not root:
            return res
        l_res = self._helper(root.left)
        r_res = self._helper(root.right)
        res[0] = max(l_res) + max(r_res)
        res[1] = root.val + l_res[0] + r_res[0]
        return res