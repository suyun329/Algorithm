n= int(input())
a=list(map(int, input().split()))
b=[]
dic = {}  #{-10: 0, -9: 1, 2: 2, 4: 3}
b = sorted(set(a))

for i in range(len(b)):
    dic[b[i]]=i
    
for j in a:
    print(dic[j], end=' ')
