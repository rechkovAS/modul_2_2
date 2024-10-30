# Функция count_calls подсчитывающая вызовы остальных функций.
calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls

# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string_ = ''):
    a = len(string_)
    b = string_.upper()
    c = string_.lower()
    string_tuple = a, b, c
    count_calls()
    return string_tuple

# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string = '', list_to_search = []):
    for i in range(len(list_to_search)):
        a = False
        x = list_to_search[i]
        x = x.lower()
        y = string.lower()
        #print(i)
        if x == y:
            a = True
            break
        #print(list_to_search)
        #print(x)
        #print(y)
    count_calls()
    return a

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
