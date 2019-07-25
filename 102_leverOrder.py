# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 方法一：递归
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        res.append([root.val])
        if not root.left and not root.right:
            return res
        left_res = self.levelOrder(root.left)
        right_res = self.levelOrder(root.right)
        
        left_len = len(left_res)
        right_len = len(right_res)
        if left_len < right_len:
            lower = left_len
            upper = right_len
            max_res = right_res
        else:
            lower = right_len
            upper = left_len
            max_res = left_res
        
        for i in range(upper):
            if i < lower:
                res.append(left_res[i]+right_res[i])
            else:
                res.append(max_res[i])
        return res

# 方法二：队列实现
class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        if not root:
            return res
        while queue:
            n = len(queue)
            tmp = []
            for _ in range(n):
                node = queue.pop()
                if node:
                    tmp.append(node.val)
                    if node.left:
                        queue.insert(0, node.left)
                    if node.right:
                        queue.insert(0, node.right)
            res.append(tmp)
        return res