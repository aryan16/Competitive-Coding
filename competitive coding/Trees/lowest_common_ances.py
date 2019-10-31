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
    
# def level_order(node):
#     queue = []
#     queue.append(node)
#     while(len(queue)>0):
#         temp_list.append(queue[0].data)
#         temp = queue.pop(0)
#         if temp.left != None:
#             queue.append(temp.left)
#         if temp.right != None:
#             queue.append(temp.right)

def lowest_common(root,n1,n2):
    if root == None:
        return None
    if root.data == n1 or root.data == n2:
        return root
    left = lowest_common(root.left,n1,n2)
    right = lowest_common(root.right,n1,n2)
    
    if left != None and right != None:
        return root
    if left != None and right == None:
        return left
    if left == None and right != None:
        return right
    if left == None and right == None:
        return None
    



root = insert(None,7)
insert(root,4)
insert(root,12)
insert(root,3)
insert(root,6)
insert(root,1)
insert(root,5)
insert(root,8)
insert(root,10)
# level_order(root)
# print(temp_list)
# show(root)
print(lowest_common(root,4,1).data)

