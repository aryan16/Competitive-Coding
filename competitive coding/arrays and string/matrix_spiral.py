list1 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
m = len(list1)
n = len(list1[0])

left = 0
right = n - 1
top = 0
down = m - 1
final = []
while(1):
    if left>right:
        break
    for i in range(left,right+1):
        final.append(list1[top][i])
    top = top + 1
    if top>down:
        break
    for i in range(top,down+1):
        final.append(list1[i][right])
    right = right - 1
    if left>right:
        break
    for i in range(right,left-1,-1):
        final.append(list1[down][i])
    down = down - 1
    if top>down:
        break
    for i in range(down,top-1,-1):
        final.append(list1[i][left])
    left = left + 1
print(final)
    
        