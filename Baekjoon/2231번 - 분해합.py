a=int(input())

for i in range(1, a+1):
    e = sum(map(int,str(i)))
    if i+e==a:
        print(i)
        break

    if i==a:
        print(0)