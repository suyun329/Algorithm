n= int(input())
a=[]

for i in range(n):
    b=list(map(int, input().split()))
    a.append(b)

a.sort()

for j, k in a:
    print(j, k)
