import sys
from collections import deque

n = int(input())
bal = deque()
cut = []

bpop = deque(enumerate(map(int, sys.stdin.readline().split())))
while bpop:
    idx, num = bpop.popleft()
    cut.append(idx+1)
    
    if num>0:
        bpop.rotate(-(num-1))
    else:
        bpop.rotate(-num)

print(*cut)
