# Задача "Рассылка писем":

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
def send_email(message, recipient, *, sender = "university.help@gmail.com"):
#message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию
# sender = "university.help@gmail.com"
    # Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",str(recipient.endswith('.ru' or '.com' or '.net')) != "True"
#             or str(sender.endswith('.com' or '.ru' or '.net')) != "True")
    if ("@" not in recipient or  "@" not in sender
            or not (recipient.endswith('.ru') or recipient.endswith('.com') or recipient.endswith('.net'))
            or not (sender.endswith('.ru') or sender.endswith('.com') or sender.endswith('.net'))):
        # то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        # Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")

        # Если же отправитель по умолчанию - university.help@gmail.com,
        # то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
#
# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!