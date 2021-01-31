HELP = """Доступные команды:
help - Напечатать справку
add - добавить задачу в список 
print - напечатать все задачи из списка"""

tasks = ['Cleaning']

print(HELP)

while True:
    # Будет выполнятся бесконечно
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите задачу: ')
        tasks.append(task)
    elif command == 'print':
        print(tasks)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break  
    else:
        # Пока не встретится ключевое слово break
        print('Неизвестная команда')
        break