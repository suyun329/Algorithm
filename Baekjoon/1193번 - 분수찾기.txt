i=int(input())

end=1
line=1


while i>end:
    line+=1
    end+=line
        
if line%2==0:
    a=i+line-end
    b=line-a+1
                    
else:
    b=i+line-end
    a=line-b+1
                
#print(a, '/', b, sep='')
print(f"{a}/{b}")
                  

