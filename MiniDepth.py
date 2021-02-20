class node:

    def __init__(self,val=0,left=None,right=None):

        self.val = 0
        self.left = left
        self.right = right




def minidepth(root):

    if root == None:

        return 0

    q=[root]

    depth = 1

    while len(q) != 0:

        for node in q:

            if node.left == None and node.right == None:

                return depth

            if node.left != None:

                q.append(node.left)

            if node.right != None:

                q.append(node.right)

            q.pop(0)

        depth += 1

    return depth




tree = node(3,node(9),node(20))

tree.right.left = node(15)
tree.right.left = node(7)

sec_tree = node(2,None,node(3,None,node(4,None,node(5,None,node(6)))))

ans_1 = minidepth(tree)

ans_2 = minidepth(sec_tree)                           
