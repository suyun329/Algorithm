import sys
n = int(sys.stdin.readline())

stack=[]

for i in range(n):
    commend = sys.stdin.readline().split()
    
    if commend[0]=='push':
        stack.append(commend[1])
        
    elif commend[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif commend[0]=='size':
        print(len(stack))
    elif commend[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif commend[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])