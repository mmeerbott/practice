#!/usr/bin/env python3
# Problem:
# https://leetcode.com/problems/path-sum/
#

import math
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool: 
        if (root is None):
            return False
        return self.checkSubtree(root, 0, targetSum)
            
    def checkSubtree(self, node: TreeNode, total: int, targetSum: int) -> bool:
        path_exists = False

        if (node.right is None and node.left is None and total + node.val == targetSum):
            return True

        if (node.left is not None):
            path_exists = path_exists or self.checkSubtree(node.left, total + node.val, targetSum)

        if (node.right is not None):
            path_exists = path_exists or self.checkSubtree(node.right, total + node.val, targetSum)

        return path_exists
