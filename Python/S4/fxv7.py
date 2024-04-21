def sumar(n):
    if n==1:
        return 1
    else:
        return n+sumar(n-1)


print(sumar(100))

#factorial m*m-1
def factorial(m):
    if m!=1:
        return m*factorial(m-1)
    else:
        return 1

print(factorial(120))