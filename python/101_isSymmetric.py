# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
    def height_Tree(self, root): # 计算树的深度
        if not root: return 0
        left_Tree_h = self.height_Tree(root.left)
        right_Tree_h = self.height_Tree(root.right)
        return max(left_Tree_h, right_Tree_h) + 1


    def l_traverse_Tree(self, l_Tree_list, root_height, root): # 递归实现先序遍历
        root_height -= 1
        if not root:
            if root_height >=  0:
                l_Tree_list.append('null')
                root_height += 1
                return
            else:
                root_height += 1
                return

        l_Tree_list.append(root.val)
        self.l_traverse_Tree(l_Tree_list, root_height, root.left)
        self.l_traverse_Tree(l_Tree_list, root_height, root.right)

    def r_traverse_Tree(self, r_Tree_list, root_height, root): # 递归实现后序遍历
        root_height -= 1
        if not root:
            if root_height >=  0:
                r_Tree_list.append('null')
                root_height += 1
                return
            else:
                root_height += 1
                return

        r_Tree_list.append(root.val)
        self.r_traverse_Tree(r_Tree_list, root_height, root.right)
        self.r_traverse_Tree(r_Tree_list, root_height, root.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        l_root_list = []; r_root_list = []
        root_height = self.height_Tree(root)
        self.l_traverse_Tree(l_root_list, root_height, root)
        self.r_traverse_Tree(r_root_list, root_height, root)
        if l_root_list == r_root_list:
            return True
        else:
            return False

Tree = binary_trees([1, 2, 2,'null', 4, 4,'null', 3, 'null', 'null', 3])
Tree1 = binary_trees(['null'])
print(Solution().isSymmetric(Tree))
print(Solution().isSymmetric(Tree1))


# 下面是方法二

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_way2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归
        def isSameTree(p, q): # 判断两个子树是否相同
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                l = isSameTree(p.left, q.right)
                r = isSameTree(p.right, q.left)
                return l and r
            else:
                return False
        
        if not root:
            return True
        else:
            return isSameTree(root.left, root.right)
        