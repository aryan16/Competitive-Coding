class Node:

    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        
temp_list = []   
def insert(node,data):
    if node == None:
        return Node(data)
    else:
        if data <= node.data:
            node.left = insert(node.left,data)
        elif data > node.data:
            node.right = insert(node.right,data)
        return node

def show(node):
    if node == None:
        return 0
    show(node.left)
    print(node.data)
    show(node.right)
    
def level_order(node):
    queue = []
    queue.append(node)
    while(len(queue)>0):
        temp_list.append(queue[0].data)
        temp = queue.pop(0)
        if temp.left != None:
            queue.append(temp.left)
        if temp.right != None:
            queue.append(temp.right)
def levelOrder(root):

    queue = []
    final = []
    temp = []
    res = []
    queue.append(root)
    final.append(root.data)
    res.append(final[:])
    while(queue):
        node = queue.pop(0)
        final.pop(0)
        if node.left:
            temp.append(node.left.data)
            queue.append(node.left)
        if node.right:
            temp.append(node.right.data)
            queue.append(node.right)
        if len(final) == 0:
            final = temp
            res.append(final[:])
            temp = []
    res.pop()
    return res


root = insert(None,7)
insert(root,4)
insert(root,12)
insert(root,3)
insert(root,6)
insert(root,1)
insert(root,5)
insert(root,8)
insert(root,10)
print(levelOrder(root))
# level_order(root)
# print(temp_list)
# show(root)

