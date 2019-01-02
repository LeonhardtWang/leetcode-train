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