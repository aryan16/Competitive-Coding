matrix = [['0','*','0','s'],['*','0','*','*'],['0','*','*','*'],['d','0','0','0']]
m = len(matrix)
n = len(matrix[0])
source = ()
dest = ()
for i in range(0,m):
    for j in range(0,n):
        if matrix[i][j] == 's':
            source = (i,j)
        elif matrix[i][j] == 'd':
            dest = (i,j)

queue = []
path = []
queue.append((source,path))
visited=[]
visited.append(source)
succ = []
final = []
while(len(queue)>0):
    point,action = queue.pop()
    if point == dest:
        final = action
        break
    if(point[0]+1 <= n-1 and matrix[point[0]+1][point[1]] != '0'):
         succ.append((point[0]+1,point[1]))

    if(point[0] - 1 >= 0 and matrix[point[0]-1][point[1]] != '0'):
        succ.append((point[0]-1,point[1]))

    if(point[1] + 1<=m-1 and matrix[point[0]][point[1]+1] != '0' ):
        succ.append((point[0],point[1]+1))
    
    if(point[1]-1>=0 and matrix[point[0]][point[1]-1] != '0'):
        succ.append((point[0],point[1]-1))
    
    for p in succ:
        if p not in visited:
            temp_path = action + [point]
            queue.append((p,temp_path))
            visited.append(p)
print(final)




