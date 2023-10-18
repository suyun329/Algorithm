import sys
input = sys.stdin.readline

n = int(input())
s=[]
for _ in range(n):
    s.append(list(map(int, input().split())))
print(s)
a=s[0][0]+max(s[1])

# for i in s:
    # a += i
