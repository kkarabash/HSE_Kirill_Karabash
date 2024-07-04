def roman_to_int(s):
    # Словарь: римская - обычная
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Переменная для накопления результата
    prev_value = 0  # Переменная для хранения предыдущего значения

    # Проходим по символам строки в обратном порядке
    for char in reversed(s):
        value = roman_values[char]  # Получаем значение текущего символа
        if value < prev_value:
            total -= value  # Если текущее значение меньше предыдущего, вычитаем его
        else:
            total += value  # В противном случае добавляем его
        prev_value = value  # Обновляем предыдущее значение

    return total


# Примеры из задания
print(roman_to_int("III"))     # Output: 3
print(roman_to_int("LVIII"))   # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994



