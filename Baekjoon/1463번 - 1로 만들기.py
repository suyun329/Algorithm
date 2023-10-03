n = int(input())
a=0
while n!=1:
    a += 1
    if n%3 == 0:
        n = n//3
        print('1', n)
    elif n%2 == 0:
        n = n//2
        print('2',n)
    else:
        n= n-1
        print('3',n)
print(a)
