k = 2
list1 = [2,3,6,3,3,3,8]
temp = 0
for i in range(0,len(list1)-1):
    if(list1[i+1]<list1[i]):
        temp = temp + 1
    if temp > k:
        break
if temp > k:
    print(False)
else:
    print(True)


