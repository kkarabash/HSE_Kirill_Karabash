def is_palindrome(number: int) -> bool:
    # Преобразуем число в строку
    num_str = str(number)
    # Проверяем, равно ли строковое представление числа его обратному
    return num_str == num_str[::-1]
print(is_palindrome(127))
