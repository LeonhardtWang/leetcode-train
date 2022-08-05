# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            root_node = TreeNode(nums[mid])
            nums_left = nums[:mid]
            nums_right = nums[mid+1:]
            root_node.left = self.sortedArrayToBST(nums_left)
            root_node.right = self.sortedArrayToBST(nums_right)
        return root_node