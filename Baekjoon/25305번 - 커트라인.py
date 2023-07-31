n, m =  map(int, input().split())
st=list(map(int, input().split()))

st.sort(reverse=True)
print(st[m-1])