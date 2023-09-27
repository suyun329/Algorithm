def factorial(n):
    if n == 0:
        return 1
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


a, b = map(int, input().split())
print(factorial(a)//(factorial(b)*factorial(a-b)))
