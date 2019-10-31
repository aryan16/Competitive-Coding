a = "abcabcdb"
d = {}
count = 0
for i in range(0,len(a)):
    d[a[i]] = -1

for i in range(0,len(a)):
    if d[a[i]] == -1:
        count = count + 1
        d[a[i]] = i
    else:
        if count <= i-d[a[i]]:
            count = i - d[a[i]]
        d[a[i]] = i 
print(count)


