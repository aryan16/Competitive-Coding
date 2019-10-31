import heapq
a = [1,2,3,1,4,5,2,3,6]
k = 3
# Solution 1
# final = []
# for i in range(0,len(a)-k+1):
#     temp = -1
#     for j in range(i,i+k):
#         if a[j]>temp:
#             temp = a[j]
#     final.append(temp)
# print(final)

# Solution 2 - Max Heap
i = 0
j = k-1
heap = a[i:j + 1] 
heapq._heapify_max(heap) 
    
# Print the maximum element from  
# the first window of size k 
print(heap[0], end =" ") 
last = a[i] 
i+= 1
j+= 1
nexts = a[j] 

while j<len(a):
    heap[heap.index(last)] = nexts
    heapq._heapify_max(heap)
    print(heap[0], end = " ")
    last = a[i] 
    i = i + 1
    j = j + 1
    if j<len(a):
        nexts = a[j]

