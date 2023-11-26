from date import name_data, body_data, today_data

def input_data():
    name = name_data()
    body = body_data()
    data = today_data()
    with open('notes.csv', 'a', encoding='utf-8') as file:
        file.write(f'{name}\n{body}\n{data}\n\n')




def print_data():
    print('Вывожу данные: \n')
    with open('notes.csv', 'r', encoding='utf-8') as file:
        data_notes = file.readlines()
        data_notes_version = []
        j = 0
        for i in range(len(data_notes)):
            if data_notes[i] == '\n' or i == len(data_notes) - 1:
                data_notes_version.append(''.join(data_notes[j:i + 1]))
                j = i
        data_notes = data_notes_version
        print(''.join(data_notes))
    return data_notes



def put_data():
    data_notes = print_data()
    print("Какую запись по счету хотите изменить?")
    number_journal = int(input('Введите номер записи: '))
    number_journal -= 1
    change_line(data_notes, number_journal)



def change_line(data_notes, number_journal):
    answer = input(f"Изменить данную запись?\n{data_notes[number_journal]}\nВведите ответ: ")
    while answer != 'да':
        number_journal = int(input('Введите номер записи: ')) - 1

    print(f"Меняем данную запись\n{data_notes[number_journal]}\n")
    
    name = data_notes[number_journal].split('\n')[0]
    body = data_notes[number_journal].split('\n')[1]

    answer = int(input(f"Какие данные Вы хотите поменять?\n"
                       f"1. Заголовок\n"
                       f"2. Заметка\n"

                       f"Введите ответ: "))
    while answer < 1 or answer > 2:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 2")
        answer = int(input(f"Какие данные Вы хотите поменять?\n"
                           f"1. Заголовок\n"
                           f"2. Заметка\n"

                           f"Введите ответ: "))
    if answer == 1:
        name = name_data()
    elif answer == 2:
        body = body_data()
    data = today_data()

    
    
    data_notes = data_notes[:number_journal] + [f'{name}\n{body}\n{data}\n'] + \
                 data_notes[number_journal + 1:]
    if number_journal + 1 == len(data_notes):
        data_notes = data_notes[:number_journal] + [f'{name}\n{body}\n{data}\n']
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_notes))
    print('Изменения успешно сохранены!')


def delete_data():
    data_notes = print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    # Можно добавить проверку, чтобы человек не выходил за пределы записи
    print(f'Удалить данную запись\n{data_notes[number_journal - 1]}')
    # print(data_notes[:number_journal - 1], data_notes[number_journal + 1:]) error
    data_notes = data_notes[:number_journal - 1] + data_notes[number_journal + 1:]
    with open('data_notes_variant.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_notes))
    print('Изменения успешно сохранены!')
















