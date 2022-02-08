i=input()

i=int(i)
a=1
n=1
if i==1:
    print(1)
else:
    while True:
        if a>=i:
            print(n)
            break
            
        else:
            a+=6*n
            n+=1
            