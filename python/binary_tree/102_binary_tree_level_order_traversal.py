__author__ = 'zhangsensen'

'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）

解法：迭代。利用队列实现层序遍历，每一层的出栈节点数等于上一层的入栈节点数。
'''

from python.binary_tree.tree_utils import build_tree

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    queue, output, level_output = [root], [], []
    in_num, out_num = 0, 1
    while len(queue) > 0 and out_num > 0:
        for i in range(out_num):
            cur_node = queue.pop(0)
            level_output.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
                in_num += 1
            if cur_node.right:
                queue.append(cur_node.right)
                in_num += 1
        output.append(level_output)
        level_output = []
        in_num, out_num = 0, in_num
    return output

if __name__ == '__main__':
    a = [1,2,3,4,"null",5]
    #a = [1,"null",2,3]
    r = build_tree(a)
    result = levelOrder(r)
    print(result)
