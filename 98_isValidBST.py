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
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, None, None)
        
    def helper(self, root, lower, upper):
        if root is None:
            return True
        if lower is not None and root.val <= lower:
            return False
        if upper is not None and root.val >= upper:
            return False
        if not self.helper(root.left, lower, root.val):
            return False
        if not self.helper(root.right, root.val, upper):
            return False
        return True


# 方法二：中序遍历
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        before_val = float('-inf')
        stack = []
        if root is None:
            return True
        stack.append(root)
        root = root.left
        while stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= before_val:
                return False
            before_val = node.val
            
            if node.right:
                stack.append(node.right)
                root = node.right.left
        return True

test = binary_trees([5,1,4,'null','null',3,6])
print(Solution2().isValidBST(test))
        