n = int(input())
a, b = [], []
a = set(map(int, input().split()))  #set - O(1)
m = int(input())
b = list(map(int, input().split())) #list - O(n)

for i in range(m):
    if b[i] in a:
        print('1')
    else:
        print('0')
        
# 1920번 - 수 찾기 [https://www.acmicpc.net/problem/1920]
