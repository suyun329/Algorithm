n, k = map(int, input().split())
w, v, sum = [], [], []
nk = 0

for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
w.append(0)
# i=0

for i in range(n):
    nk += w[i]
    print(nk)
    if nk <= k and nk+w[i+1] > k:
        sum.append(nk)
        nk = 0
            
print(sum)
