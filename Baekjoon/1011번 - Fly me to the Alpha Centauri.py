T=int(input())

for i in range(T):
    x, y=map(int, input().split())
    
    M=y-x
    a=2 #1,2 기준이 되는 값
    b=2 #2*n n에 해당하는 것
    first=1 #범위 최솟값
    Sum=2 #11 22 33 44....들의 합
        
    while True: 
        if(first<=M and Sum>=M):
            if ((Sum-b+1)<M and Sum>=M):
                print(a)
            else:
                print(a-1)
            break
                
        else:
            a=2*b
            b+=1
            first=Sum+1
            Sum+=a