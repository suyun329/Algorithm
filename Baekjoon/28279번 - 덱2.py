import sys
from collections import deque

n = int(input())
deque = deque()

for _ in range(n):
    ment = list(map(int, sys.stdin.readline().split()))

    if ment[0] == 1:
        deque.appendleft(ment[1])
    elif ment[0] == 2:
        deque.append(ment[1])
    elif ment[0] == 3:
        if deque:
            print(deque.popleft())
        else:
            print('-1')
    elif ment[0] == 4:
        if deque:
            print(deque.pop())
        else:
            print('-1')
    elif ment[0] == 5:
        print(len(deque))
    elif ment[0] == 6:
        if deque:
            print('0')
        else:
            print('1')
    elif ment[0] == 7:
        if deque:
            print(deque[0])
        else:
            print('-1')
    else:
        if deque:
            print(deque[-1])
        else:
            print('-1')
        
        
