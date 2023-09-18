while True:
    T = input()
    s2 = []
    if T == '.':
        break
        
    for j in T:
        if j=='(' or j=='[':
            s2.append(j)
                
        #)    
        elif j==')':
            if s2 and s2[-1]=='(':
                s2.pop()
            else:
                s2=[')']
                break
        #]        
        elif j==']':
            if s2 and s2[-1]=='[':
                s2.pop()
            else:
                s2=[']']
                break
                
    if s2:
           print('no')
    else:
           print('yes')

