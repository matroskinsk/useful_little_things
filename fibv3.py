# Fibonachi v3
n = int(input()) # объем последовательности
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
    print(a, end=' ')
def fib(x): # Нное число фибоначи рекурсия
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib(x - 1) + fib(x - 2)
x = int(input())
print(fib(x))