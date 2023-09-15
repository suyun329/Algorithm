n= int(input())
a=[]
for i in range(n):
    b=input()
    a.append(b)

for j in a:
    s=[]
    for k in range(len(j)):  
        if j[k]=='(':
            s.append(j[k])
        else: # ) 들어왔을 때 스택이 비어있으면 no로 끝, 아니면 pop후 계속
            if s:
                s.pop()
            else:
                s=[')']
                break
    if s:
        print('NO')
    else:
        print('YES')
