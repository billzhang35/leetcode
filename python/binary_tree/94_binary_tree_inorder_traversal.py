__author__ = 'zhangsensen'

'''
给定一个二叉树，返回它的 中序 遍历。

解法一：递归
解法二：迭代
'''

from python.binary_tree.tree_utils import build_tree

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    left_traverse = inorderTraversal(root.left)
    right_traverse = inorderTraversal(root.right)
    return left_traverse + [root.val] + right_traverse


def inorderTraversal2(root):
    if not root:
        return []
    stack, output = [], []
    cur_node = root
    while len(stack) > 0 or cur_node:
        if cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
            continue
        cur_node = stack.pop()
        output.append(cur_node.val)
        cur_node = cur_node.right
    return output


if __name__ == '__main__':
    a = [1,2,3,4,"null",5]
    r = build_tree(a)
    result = inorderTraversal2(r)
    print(result)






