# 树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 输入列表，生成二叉树
def binary_trees(input):
    if not input:return None
    root = TreeNode(input[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodeQueue[front]
        front += 1

        item = input[index]
        index += 1
        if item != 'null':
            node.left = TreeNode(item)
            nodeQueue.append(node.left)
        
        if index >= len(input):break
        
        item = input[index]
        index += 1
        if item != 'null':
            node.right = TreeNode(item)
            nodeQueue.append(node.right)
    return root


# 方法一：递归
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        if root is None:
            return res
        
        left = self.inorderTraversal(root.left)
        res.extend(left)
        res.append(root.val)
        right = self.inorderTraversal(root.right)
        res.extend(right)
        return res

# 方法二：遍历（栈）
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                root = node.right.left
        return res

test = binary_trees([1,'null',2,3])
print(Solution2().inorderTraversal(test))