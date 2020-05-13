__author__ = 'zhangsensen'

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def build_tree(node_list):
    if len(node_list) == 0:
        return None
    root = TreeNode(node_list.pop(0))
    queue = [root]
    while len(queue) > 0 and len(node_list) > 0:
        cur_node = queue.pop(0)
        cur_value = node_list.pop(0)
        if cur_value != "null":
            new_node = TreeNode(cur_value)
            cur_node.left = new_node
            queue.append(new_node)
        if len(node_list) == 0:
            break
        cur_value = node_list.pop(0)
        if cur_value != "null":
            new_node = TreeNode(cur_value)
            cur_node.right = new_node
            queue.append(new_node)
    return root

def preorderTraversal(root):
    if not root:
        return []
    left_traverse = preorderTraversal(root.left)
    right_traverse = preorderTraversal(root.right)
    return [root.val] + left_traverse + right_traverse

def inorderTraversal(root):
    if not root:
        return []
    left_traverse = inorderTraversal(root.left)
    right_traverse = inorderTraversal(root.right)
    return left_traverse + [root.val] + right_traverse

def postorderTraversal(root):
    if not root:
        return []
    left_traverse = postorderTraversal(root.left)
    right_traverse = postorderTraversal(root.right)
    return left_traverse + right_traverse + [root.val]

if __name__ == '__main__':
    a = [1,2,3,4,"null",5]
    r = build_tree(a)
    print(r.right.left.val)
