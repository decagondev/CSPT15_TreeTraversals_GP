"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
*Note: assume that there will not be any duplicates in the tree.*
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
Output:
    5
   / \
  7  22
    /  \
   13   9
"""

pre_order = [5, 7, 22, 13, 9]

in_order = [7, 5, 13, 22, 9]

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    root = TreeNode(preorder.pop(0))
    i = inorder.index(root.val)
    left = inorder[0:i]
    right = inorder[i+1:]
    if len(left):
        root.left = build_tree(preorder, left)
    if len(right):
        root.right = build_tree(preorder, right)
    return root


tree1 = build_tree(pre_order, in_order)

print("Done!")
