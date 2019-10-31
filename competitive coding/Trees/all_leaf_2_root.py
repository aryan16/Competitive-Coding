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
arr = []
final = []
def root_leaf(root):
    if root == None:
        return 
        
    arr.append(str(root.data))
    root_leaf(root.left)
    if root.left == None and root.right == None:
        print(arr)
    root_leaf(root.right)
    final.append(arr)
    arr.pop(-1)
    if len(arr) == 0:
        return final


root = insert(None,7)
insert(root,4)
insert(root,12)
insert(root,3)
insert(root,6)
insert(root,1)
insert(root,5)
insert(root,8)
insert(root,10)
print(root_leaf(root))
# level_order(root)
# print(temp_list)
# show(root)

