n = int(input())
w = []
dp = [0]*(n+1)
for _ in range(n):
    w.append(int(input()))
dp[1] = w[0]
if n >= 2:
    dp[2] += w[1]
    for i in range(3, n+1):
        dp[i] = max()

print(dp[n])

# 참고 - https://bio-info.tistory.com/156
