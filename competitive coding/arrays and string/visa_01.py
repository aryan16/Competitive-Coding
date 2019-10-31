s = '<>><'
stack = []
k = 2
d = {}
d['>'] = '<'
temp = 0
flag = True
for i in range(0,len(s)):
    if s[i] == '<':
        temp = i
        stack.append('<')
        break
    else:
        k = k - 1
    if k<0:
        flag = False
        break
temp = temp + 1
if flag == True and len(stack) > 0:
    while(temp<len(s)):
        if s[temp] == '<':
            stack.append('<')
            temp = temp + 1
        else:
            if len(stack)>0:
                stack.pop(0)
            else:
                k = k - 1
                if k<0:
                    flag = False
                    break
            temp = temp + 1
if(len(stack)>0):
    flag = False
print(flag)


           