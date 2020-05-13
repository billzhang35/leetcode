__author__ = 'zhangsensen'

'''
给定一个二叉树，返回它的 后序 遍历。

解法一：递归
解法二：迭代。利用中序的方法，增加一个dict记录二次进栈
解法三：迭代。利用前序的方法，左子树先进栈，得到的结果逆序即为后序
'''

from python.binary_tree.tree_utils import build_tree

def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    left_traverse = postorderTraversal(root.left)
    right_traverse = postorderTraversal(root.right)
    return left_traverse + right_traverse + [root.val]


def postorderTraversal2(root):
    if not root:
        return []
    stack, output = [], []
    cur_node = root
    second_push = {}
    while len(stack) > 0 or cur_node:
        if cur_node:
            stack.append(cur_node)
            cur_node = cur_node.left
            continue
        cur_node = stack.pop()
        if cur_node.right and cur_node not in second_push:
            stack.append(cur_node)
            second_push[cur_node] = 1
            cur_node = cur_node.right
        else:
            output.append(cur_node.val)
            cur_node = None
    return output


def postorderTraversal3(root):
    if not root:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop()
        output.append(root.val)
        if root.left is not None:
            stack.append(root.left)
        if root.right is not None:
            stack.append(root.right)
    return output[::-1]


if __name__ == '__main__':
    a = [1,2,3,4,"null",5]
    #a = [1,"null",2,3]
    r = build_tree(a)
    result = postorderTraversal3(r)
    print(result)






