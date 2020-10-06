'''
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree,
with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sum_left_leaves(self, root):
      return self._helper(True, root.left) + self._helper(False, root.right)

    def _helper(self, is_left, curr):
      if not curr:
        return 0
      if not curr.left and not curr.right:
        if is_left:
          return curr.val
        else:
          return 0
      return self._helper(True, curr.left) + self._helper(False, curr.right)

    def sum_left_leaves2(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sum_left_leaves2(root.right)
        return self.sum_left_leaves2(root.left) + self.sum_left_leaves2(root.right)


    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        return self._dfs(target, root)

    def _dfs(self, sum, curr):
      if not curr:
        return False
      if sum - curr.val == 0:
        return True
      return self._dfs(sum - curr.val, curr.left) or self._dfs(sum-curr.val, curr.right)


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        from collections import deque
        queue = deque([root])
        left_leaves_sum = 0
        if not root:
            return 0
        while queue:
            cur_root = queue.popleft()
            if cur_root.left:
                if not cur_root.left.left and not cur_root.left.right:
                    left_leaves_sum += cur_root.left.val
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        return left_leaves_sum

'''
    3
   / \
  9  20
    /  \
   15   7

target = 30, return True (3, 20, 7)
'''


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

s = Solution()
# print(s.sum_left_leaves(t1))
print(s.hasPathSum(t1, 30))


