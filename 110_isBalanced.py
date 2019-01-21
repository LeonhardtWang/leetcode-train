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

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            return max(l, r) + 1
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        l = root.left
        r = root.right
        if abs(self.maxDepth(l) - self.maxDepth(r)) > 1:
            return False
        else:
            if (not l) or (not r):
                if not l:
                    if self.maxDepth(r) <= 1:
                        return True
                    else:
                        return False
                else:
                    if self.maxDepth(l) <= 1:
                        return True
                    else:
                        return False
            return self.isBalanced(l) and self.isBalanced(r)

test_tree = binary_trees([3,9,20,'null','null',15,7])
print(Solution().isBalanced(test_tree))