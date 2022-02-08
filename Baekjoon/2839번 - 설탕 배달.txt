a=int(input())

num1=0
while a>=0:
    if a%5==0:
        print(num1+(a//5))
        break
    else:
        a=a-3
        num1+=1
else:
    print('-1')