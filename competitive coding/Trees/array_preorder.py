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
def preorder(arr):
    stack = []
    stack.append(arr[0])
    stack.append(arr[1])
    flag = 0
    leave = 0
    for i in range(2,len(arr)):
        if(arr[i]<arr[0]):
            if flag == 0:
                if(arr[i]<arr[i-1] and arr[i]<arr[i-2] and arr[i-1]>arr[i-2]):
                    leave = 1
                    break
                else:
                    stack.append(arr[i])
            else:
                leave = 1
                break
        else:
            flag = 1
            if(arr[i]<arr[i-1] and arr[i]<arr[i-2] and arr[i-1]>arr[i-2]):
                leave = 1
                break
            else:
                stack.append(arr[i])
    if leave == 1:
        print('NO')
    else:
        print('YES')


# root = insert(None,7)
# insert(root,4)
# insert(root,12)
# insert(root,3)
# insert(root,6)
# insert(root,1)
# insert(root,5)
# insert(root,8)
# insert(root,10)
# level_order(root)
# print(temp_list)
# show(root)
pre1 = [40 , 30 , 35 , 20 ,  80 , 100] 
preorder(pre1)
pre1 = [40 , 30 , 35 , 36 , 32, 80, 100] 
preorder(pre1)

