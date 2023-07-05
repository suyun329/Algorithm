import sys

n = int(sys.stdin.readline())

a=[]
for i in range(n):
    b = int(sys.stdin.readline())
    a.append(b)

a=sorted(set(a))
for j in range(len(a)):
    print(a[j])