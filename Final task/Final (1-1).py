def fib(stop_index):
    a, b = 0, 1
    current_index = 0
    while current_index < stop_index:
        yield a
        a, b = b, a + b
        current_index += 1

# Пример
stop_index = 10
for number in fib(stop_index):
    print(number)