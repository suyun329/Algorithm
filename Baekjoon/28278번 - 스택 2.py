import sys
n = int(sys.stdin.readline())

stack=[]

for i in range(n):
    commend = sys.stdin.readline().split()
    
    if commend[0]=='1':
        stack.append(commend[1])
        
    elif commend[0]=='2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif commend[0]=='3':
        print(len(stack))
    elif commend[0]=='4':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif commend[0]=='5':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])