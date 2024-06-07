def is_palindrome(number: int) -> bool:
    num_str = str(number)
    return num_str == num_str[::-1]
# числа ниже как пример
print(is_palindrome(127))
print(is_palindrome(131))