import math

a, b, v=input().split()
a=int(a)
b=int(b)
v=int(v)

day=(v-b)/(a-b)
    
print(math.ceil(day))
    