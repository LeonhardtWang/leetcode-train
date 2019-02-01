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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 方法一：自己想的,复杂了
    def search_parents(self, pare_lis, root, root_raw, val): # 找所有父节点的值
        if (root.left and root.left.val == val) or (root.right and root.right.val == val):
            pare_lis.append(root.val)
            self.search_parents(pare_lis, root_raw, root_raw, root.val)
        else:
            if root.left:
                self.search_parents(pare_lis, root.left, root_raw, val)
            if root.right:
                self.search_parents(pare_lis, root.right, root_raw, val)

    def find_val_node(self, root, val): # 返回根节点值为val的Tree
        if root.val == val:
            return root
        else:
            if root.left:
                root_left_res = self.find_val_node(root.left, val)
                if root_left_res:return root_left_res
            if root.right:
                root_right_res = self.find_val_node(root.right, val)
                if root_right_res:return root_right_res

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parents_p_lis = [p.val];parents_q_lis = [q.val]
        self.search_parents(parents_p_lis, root, root, p.val)
        self.search_parents(parents_q_lis, root, root, q.val)
        for i in range(min(len(parents_p_lis), len(parents_q_lis))):
            if parents_p_lis[-i-1] != parents_q_lis[-i-1]:
                i -= 1
                break        
        return self.find_val_node(root, parents_p_lis[-i-1])
    
    # 方法二
    '''
    #两个node，一个大于root，一个小于root，那么它们必定在root两边，共同的ancestor是root
    #两个node，都比node小，到左边去寻找，那么先找到那个必定是common ancestor
    #两个node，都比node大，类似....
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
    '''

test = binary_trees([6,2,8,0,4,7,9,'null','null',3,5,11,12,13,14])
test_res = Solution().lowestCommonAncestor(test, binary_trees([3]), binary_trees([5]))
print('end')