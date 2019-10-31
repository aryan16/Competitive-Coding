list1 = [1,3,10,15]
list2 = [9,10,11,12]
# Solution 1 space complexity : o(n)
# p = 0
# q = 0
# final = []
# while(1):
#     if list1[p]<list2[q]:
#         final.append(list1[p])
#         p = p + 1
#     else:
#         final.append(list2[q])
#         q = q + 1
#     if p == len(list1) or q == len(list2):
#         break
# print(p)
# print(final)
# if p != len(list1):
#     for i in range(p,len(list1)):
#         final.append(list1[i])
# if q != len(list2):
#     for i in range(q,len(list2)):
#         final.append(list2[i])
# print(final)


# Solution 2 Space Complexity : o(1)
p = 0
for i in range(0,len(list1)):
    if(list2[p]<list1[i]):
        temp = list1[i]
        list1[i] = list2[p]
        list2[p] = temp
        j = 0
        while(1):
            if j == len(list2)-1:
                break
            if list2[j]>list2[j+1]:
                temp = list2[j+1]
                list2[j+1] = list2[j]
                list2[j] = temp
            j = j+1
            
print(list1)
print(list2)