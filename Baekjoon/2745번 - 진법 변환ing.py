n, t = input().split()
n = list(n)
t = int(t)
a = []
c = 0
n.reverse()
print(n)
for i in range(len(n)):
    if n[i] >= 'A' or n[i] <= 'Z':
        b= ord(n[i])-55
        a.append(b)
        print(b)
    print(b, t**(len(n)-1-i), (len(n)-1-i))
    c += b*(t**(len(n)-1-i))
    
print(c)