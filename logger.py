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



def change_line(dataFile, numberRow):
    answer = input(f"Изменить данную запись?\n{dataFile[numberRow]}\nВведите ответ: ")
    while answer != 'да':
        numberRow = int(input('Введите номер записи: ')) - 1

    print(f"Меняем данную запись\n{dataFile[numberRow]}\n")

    name = dataFile[numberRow].split('\n')[0]
    body = dataFile[numberRow].split('\n')[1]

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




    data_first = dataFile[:numberRow] + [f'{name}\n{body}\n{today_data()}'] + dataFile[numberRow + 1:]
    if numberRow + 1 == len(dataFile):
        data_first = dataFile[:numberRow] + [f'{name}\n{body}\n{today_data()}\n']
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_first))
    print('Изменения успешно сохранены!')



def delete_data():
    data_notes = print_data()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input('Введите номер записи: '))
    
    print(f'Удалить данную запись\n{data_notes[number_journal - 1]}')
    
    data_notes = data_notes[:number_journal - 1] + data_notes[number_journal:]
    with open('notes.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_notes))
    print('Изменения успешно сохранены!')
















