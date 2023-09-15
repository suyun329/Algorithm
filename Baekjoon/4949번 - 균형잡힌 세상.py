import sys
input = sys.stdin.readline

while True:
    T = input()
    s2 = []
    if T == '.':
        break
    else:
        for j in T:
            #( or [
            if j=='(' or j=='[':
                s2.append(j)
                
            #)    
            elif j==')':
                if not s2 or s2[-1]=='[':
                    s2=[')']
                    break
                else:
                    s2.pop()
            #]        
            elif j==']':
                if s2 or s2[-1]=='(':
                    s2=[']']
                    break
                else:
                    s2.pop()
                
        if s2:
            print('NO')
        else:
            print('YES')


#state: 런타임 에러
