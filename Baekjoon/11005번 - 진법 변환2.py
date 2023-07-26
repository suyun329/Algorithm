n, t =  map(int, input().split())
a = []
c = ''
while n>0:
    b=n%t
    if b>9:
        b=b+55
        c+=chr(b)
    else:
        c+=str(b)
    n=n//t
print(c[::-1])
