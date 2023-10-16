T=int(input())

for i in range(T):
    a=int(input())*0.01
    q= d= n= p=0
    while float(a)>=0.25:
        a=float(a)-0.25
        q=q+1
        
    while round(a, 2)>=0.10:
        a=a-0.10
        d=d+1

    while round(a, 2)>=0.05:
        a=a-0.05
        n=n+1
        
    if round(a, 2)>=0.01:
        a=str(round(a, 2))
        p=a[3]
        
    print(q, d, n, p)
