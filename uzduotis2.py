
def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        suma = a + b
        a = b
        b = suma

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

