import sys

n= int(sys.stdin.readline())
a=[0]*10001

for i in range(n):
    s=int(sys.stdin.readline())
    a[s]+=1
for j in range(10001):
    if a[j]!=0:
        for k in range(a[j]):
            print(j)