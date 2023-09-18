import sys

n = int(input())
a = list(map(int, input().split()))
b = []

for j in range(n):
    a1 = a
    if a1[0] == min(a1):
        a.pop(0)
        
    else:
        b.append(a[0])
        a.pop(0)
        if b[-1]!=n and a1[-1]!=n:
            print('Sad')
            sys.exit()
        n = n-1
        
print('Nice')

state: wrong answer
