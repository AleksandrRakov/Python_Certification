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
















