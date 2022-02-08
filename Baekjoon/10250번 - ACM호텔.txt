T=int(input())

for i in range(T):
    h, w, n=map(int, input().split())
    
    if n%h==0:
        f=h
        l=n//h
    else:
        f=(n%h)
        l=(n//h)+1
    
    print(f*100+l)