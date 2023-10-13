
# 시행착오 - 시간초과

n = int(input())
a, b, r = [], [], []
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    r.append(a.count(i))

print(*r, sep=' ')

# 참고 https://chancoding.tistory.com/45
