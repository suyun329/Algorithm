n = int(input())
dp = [0]*(n+1)
w = []
for _ in range(n):
    w.append(int(input()))
dp[1] = w[0]
if n >= 2:
    dp[2] = w[0]+w[1]  # dp[2]+=w[1] (X)
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+w[i-2]+w[i-1], dp[i-2]+w[i-1], dp[i-1]) #sum(w[i-2:i] == w[i-2]+w[i-1]

print(dp[n])

# 참고 - https://bio-info.tistory.com/156
