# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：递归（回溯法）
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self._helper(root, p, q)
        return self.ans
    
    def _helper(self, root, p, q):
        if not root:
            return False
        left = self._helper(root.left, p, q)
        right = self._helper(root.right, p, q)
        mid = root == p or root == q
        
        if left + right + mid >= 2:
            self.ans = root
        return left or right or mid

    
# 方法二：使用父指针迭代
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent_dict = {root:None}
        self._helper(root, parent_dict)
        parent_p = [p]
        parent_q = [q]
        while p:
            p = parent_dict[p]
            parent_p.append(p)
        while q:
            q = parent_dict[q]
            parent_q.append(q)
        for p in parent_p:
            if p in parent_q:
                return p
    
    def _helper(self, root, parent_dict):
        if not root:
            return
        left = root.left
        right = root.right
        if left:
            parent_dict[left] = root
        if right:
            parent_dict[right] = root
        self._helper(left, parent_dict)
        self._helper(right, parent_dict)