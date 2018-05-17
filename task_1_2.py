# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3

def compare_str(str1, str2):
    if str1 == str2:
        result = 1
    elif str1 != str2 and len(str1) > len(str2):
        result = 2
    elif str1 != str2 and str2 == 'learn':
        result = 3
    else:
        result = 'Входные данные не подходят под условия сравнения!'
    return result
s1 = input('Первая строка: ')
s2 = input('Вторая строка: ')
print(compare_str(s1,s2))

