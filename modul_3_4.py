# Задача "Однокоренные":
def single_root_words(root_word, *other_words):
# Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.

# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []
# При помощи цикла for переберите предполагаемо подходящие слова.
    for i in range(len(other_words)):
        # print(root_word.lower())
        # print(other_words[i].lower())
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])

    return same_words
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']