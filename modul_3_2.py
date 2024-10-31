# Создаем функцию send_email, которая принимает 2 обычных аргумента:
# сообщение (message) и получатель (recipient)
# и один обязательно именованный аргумент со значением по умолчанию - отправитель (sender).

def send_email(message, recipient, sender="university.help@gmail.com"):

# Проверяем корретность e-mail отправителя и получателя.
# Если строка recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то выводится на экран (в консоль) строка: "Невозможно отправить письмо с адреса <sender>
# на адрес <recipient>."
    if ('@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) or '@' not in sender
            or not sender.endswith(('.com', '.ru', '.net'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
# Проверяем корректность на отправку самому себе.
# Если sender и recipient совпадают, то выводится "Нельзя отправить письмо самому себе"
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе")
# Проверяем корректность на отправителя по умолчанию.
# Если отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
# "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
# В противном случае будет выведено сообщение:
# "Нестандартный отправитель. Письмо отправлено с адреса <sender> на адрес <recipient>."
    elif sender != "university.help@gmail.com":
        print(f"Нестандартный отправитель. Письмо отправлено с адреса {sender} на адрес {recipient}.")
#                         Вывод результатов:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес eva@gmail.com
send_email('message', 'eva@gmail.com')
# Нестандартный отправитель. Письмо отправлено с адреса info@mail.ru на адрес elena@mail.ru
send_email('message', 'elena@mail.ru', 'info@mail.ru')
# Невозможно отправить письмо с адреса teacher@gmail.uk на адрес student@mail.ru
send_email('message', 'student@mail.ru', 'teacher@gmail.uk')
# Нельзя отправить письмо самому себе!
send_email('message', 'university.help@mail.ru', 'university.help@mail.ru')