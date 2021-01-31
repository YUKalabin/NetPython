today = list()
tomorrow = list()
other = list()
todos = dict()

RANDOM_TASK = 'Написать письмо Гвидо'

HELP = """Доступные команды:
help - Напечатать справку
todo - добавить задачу в список 
print - напечатать все задачи из списка
exit - выход
random - добавить случайную задачу на заданную дату
"""

tasks = ['Cleaning']

print(HELP)

def add_todo(date, task):
    date = input('Введите дату: ')
    task = input('Введите задачу: ')
    if date in todos:
        todos[date].append(task)
    else:
        todos[date] = [task]
    print(f'Задача {task} добавлена на дату {date}')




stop = False # Маркер завершения цикла
while not stop:
    # Будет выполнятся бесконечно
    command = input('Введите команду:\n ')
    if command == 'help':
        print(HELP)
    elif command == 'todo':
        date = input('Введите дату: ')
        task = input('Введите задачу: ')
        add_todo(date, task)
    elif command == 'print':
        date = input('Введите дату: ')
        if date in todos:
            print(date)
        else:
            print(f'Задач на дату {date} нет.')
        print(tasks)
    elif command == 'random':
        date = input('Введите дату: ')
        add_todo(date, RANDOM_TASK)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        stop = True
    else:
        # Пока не встретится ключевое слово break
        print('Неизвестная команда')
        stop = True
