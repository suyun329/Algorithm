while True:
    T = input()
    s = []
    if T == '.':
        break
    else:
        for i in T:
            if i=='[' or i==']' or i=='(' or i==')':
                s.append(i)
        
        s2 = []
        for j in s:
            #( or [
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
            print('NO')
        else:
            print('YES')


#state: wrong answer
