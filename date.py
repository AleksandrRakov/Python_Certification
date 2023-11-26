from datetime import datetime
def name_data():
    name = input('Заголовок: ')
    return name


def body_data():
    body = input('Заметка: ')
    return body


def today_data():
    today = datetime.now()
    return today

