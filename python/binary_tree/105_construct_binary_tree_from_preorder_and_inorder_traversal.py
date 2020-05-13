__author__ = 'zhangsensen'

'''
根据一棵树的前序遍历与中序遍历构造二叉树。

解法：迭代。利用队列实现层序遍历，每一层的出栈节点数等于上一层的入栈节点数。
'''

from python.binary_tree.tree_utils import *


def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) == 0 or len(preorder) != len(inorder):
        return None
    n = len(preorder)
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: idx + 1], inorder[0: idx])
    root.right = buildTree(preorder[idx + 1: n], inorder[idx + 1: n])
    return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # r = build_tree(a)
    result = buildTree(preorder, inorder)
    print(postorderTraversal(result))
