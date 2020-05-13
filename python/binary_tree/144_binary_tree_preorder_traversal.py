__author__ = 'zhangsensen'

'''
给定一个二叉树，返回它的 前序 遍历。

解法一：递归
解法二：迭代
'''

from python.binary_tree.tree_utils import build_tree

def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    left_traverse = preorderTraversal(root.left)
    right_traverse = preorderTraversal(root.right)
    return [root.val] + left_traverse + right_traverse


def preorderTraversal2(root):
    if not root:
        return []
    stack, output = [root], []
    while len(stack) > 0:
        cur_node = stack.pop()
        output.append(cur_node.val)
        if cur_node.right:
            stack.append(cur_node.right)
        if cur_node.left:
            stack.append(cur_node.left)
    return output


if __name__ == '__main__':
    a = [1,2,3,4,"null",5]
    r = build_tree(a)
    result = preorderTraversal2(r)
    print(result)






