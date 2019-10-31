class Node:

    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
    

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
    

def smallest(node):
    # static int temp
    if node.left == None:
        return node.data
    return smallest(node.left)
    # return node.data
    


root = insert(None,5)
insert(root,6)
insert(root,8)
insert(root,3)
insert(root,2)
insert(root,4)
# show(root)
min_val = smallest(root)
print(min_val)
