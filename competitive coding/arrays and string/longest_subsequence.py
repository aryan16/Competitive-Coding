list1 = [50,30,7,40,80]
temp = [1]*len(list1)
print(temp)
for i in range(1,len(list1)):
    for j in range(0,i):
        if list1[i]>list1[j]:
            if temp[i] < temp[j] + 1:
                temp[i] = 1 + temp[j]
print(temp)
print(max(temp))

