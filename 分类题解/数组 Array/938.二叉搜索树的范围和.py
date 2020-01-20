# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
#
# 二叉搜索树保证具有唯一的值。
#
#  
#
# 示例 1：
#
# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32
# 示例 2：
#
# 输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# 输出：23

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 搜索所有节点值的和，可用一个递归函数帮忙
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val: # 这里要用if而不是elif，因为每次都要判断
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
