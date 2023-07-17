n = int(input())
s = []
for i in range(n):
    a = input()
    if a not in s:
        s.append(a)
s=sorted(s)
s.sort(key=len)

print(*s, sep='\n')