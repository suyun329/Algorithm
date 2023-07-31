n= int(input())
p=[]

for i in range(n):
    a, b =map(str, input().split())
    p.append((int(a), b))
p.sort(key = lambda x : x[0])

for j in range(n):
    print(p[j][0], p[j][1])