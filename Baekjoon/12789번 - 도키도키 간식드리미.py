import sys

n = int(input())
a = list(map(int, input().split()))
b = []
target = 1
while a:
    a1 = a
    
    if a1[0] == target:
        a.pop(0)
        target+=1
    else:
        if b and b[-1] == target:
            b.pop(-1)
            target+=1
        else:
            b.append(a[0])
            a.pop(0)
            
if not b or b == sorted(b, reverse=True):
    print('Nice')
else:
    print('Sad')
        

###시행착오
##for -> while, b 스택에 target 있을 경우 추가

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
