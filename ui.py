from logger import input_data, print_data, put_data, delete_data



def interface():
    command = -1
    while command != 5:
        print('Заметки')
        print('Доброго времени суток! Что вы хотите сделать?\n'
              '1. Создать запись\n'
              '2. Вывести все записи\n'
              '3. Изменить запись\n'
              '4. Удалить запись\n'
              '5. Выход')
        command = int(input("Введите номер операции: "))

        while command < 1 or command > 5:
            print('Некорректный ввод, попробуйте еще раз')
            command = int(input("Введите номер операции: "))

        if command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            put_data()
        elif command == 4:
            delete_data()
        elif command == 5:
            print("Спасибо, что воспользовались нашим сервисом. Всего хорошего!")