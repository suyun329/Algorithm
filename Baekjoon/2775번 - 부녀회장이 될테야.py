T=int(input())

for i in range(T):
    a=int(input())
    b=int(input())
    num=[[]]
    
    for q in range(b+1):
        num[0].append(q)
    
    for k in range(1, a+1): #1 2, 1
        num.append([0])
        for h in range(1, b+1): #1 2 3
            num[k].append(num[k-1][h]+num[k][h-1])
    print(num[a][b])