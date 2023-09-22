from collections import deque

a, n = map(int, input().split())
peo = deque([])
cut = []
for i in range(a):
    peo.append(i+1)

while len(peo) > 0:
    for _ in range(n-1):
        peo.append(peo.popleft())
    cut.append(peo.popleft())

print('<', end='')
print(*cut, sep=', ', end='>')
