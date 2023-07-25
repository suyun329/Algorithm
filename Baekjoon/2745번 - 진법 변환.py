n, t = input().split()
n = list(n)
t = int(t)
c = 0

for i in range(len(n)):
    if n[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        b= ord(n[i])-55
        c += b*(t**(len(n)-1-i))
    else:
        b= int(n[i])
        c += b*(t**(len(n)-1-i))

print(c)