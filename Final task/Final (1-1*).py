def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Пример:
n = 100  # На каком номере остановиться
fib_gen = fibonacci_sequence(n)
for num in fib_gen:
    print(num)