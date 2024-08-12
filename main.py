def send_email(message, recipient, sender = "university.help@gmail.com"):
    
    if sender == 'university.help@gmail.com':
        message = 'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
    elif sender != recipient:
        message = 'Нельзя отправить письмо самому себе!'
    elif ("@"and(".com"or".ru"or".net")) not in (recipient or sender) or("@" or(".com"or"ru"or".net")) not in (recipient or sender):
        message = 'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    else:
        message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'
    print(message)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru')

