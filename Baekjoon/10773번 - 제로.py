import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    inp=int(sys.stdin.readline())
    if inp==0:
        num.pop()
    else:
        num.append(inp)

print(sum(num))