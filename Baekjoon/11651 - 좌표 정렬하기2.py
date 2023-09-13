n= int(input())
a=[]

for i in range(n):
    b=list(map(int, input().split()))
    a.append(b)

a.sort(key = lambda x: (x[1], x[0]))

for j, k in a:
    print(j, k)
