account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

try:
    input_key = input('Введите ключ (name или account): ').lower()
    print(f"Значение ключа {input_key} для юзера 1 = {user1[input_key]}")
    print(f"Значение ключа {input_key} для юзера 2 = {user2[input_key]}")
    print(f"Значение ключа {input_key} для юзера 3 = {user3[input_key]}")
    print(f"Значение ключа {input_key} для юзера 4 = {user4[input_key]}")
except KeyError:
    print('Введенный ключ не найден')

# В постановке задачи нет условия, что программа должна прерваться,
# если ключ не найден, поэтому далее заведен отдельный try/except,
# чтобы программа продолжилась при отсутствии ключа

try:
    input_num = input('Введите порядковый номер: ')
    check = '1,2,3,4'.find(input_num) # проверяем, есть ли введенный номер в нашем списке из 4 пользователей
    check = 1 / (check + 1) # если номера нет, то выйдем по except
    input_num = int(input_num)
    user_data = user_list[input_num - 1]
    print(f'Данные по юзеру № {input_num}:')
    print(f"Имя: {user_data['name']}")
    print(f"Возраст: {user_data['age']}")
    print(f"Логин: {user_data['account']['login']}")
    print(f"Пароль: {user_data['account']['password']}")
    
    # В постановке задачи не указано, что программа должна продолжаться, если пользователь
    # не найден на предыдущем этапе по порядковому номеру, поэтому продолжаем в рамках
    # текущего try
    input_num = input('Введите номер юзера, которого нужно переместить в конец: ')
    check = '1,2,3,4'.find(input_num) # проверяем, есть ли введенный номер в нашем списке из 4 пользователей
    check = 1 / (check + 1) # если номера нет, то выйдем по except
    input_num = int(input_num)
    new_user_list = user_list.copy() # создаем копию первоначального списка
    user_to_move = new_user_list.pop(input_num - 1) # вырезаем пользователя из нового списка
    new_user_list.append(user_to_move) # и вставляем в конец нового списка
    print(f"Юзер № {input_num} с именем {user_to_move['name']} был перемещен в конец списка")
    # Неясно, в каком именно виде нужно вывести группу до и после, предлагаю имена в строку
    print(f"Список до изменений (имена по порядку): {user_list[0]['name']}, {user_list[1]['name']}, {user_list[2]['name']}, {user_list[3]['name']}")
    user_list = new_user_list # получаем значения для изменения user_list
    print(f"Список после изменений (имена по порядку): {user_list[0]['name']}, {user_list[1]['name']}, {user_list[2]['name']}, {user_list[3]['name']}")
except ZeroDivisionError:
    print('Пользователь с указанным номером не найден')
except ValueError: # если пользователь введет например дробный порядковый номер
    print('Пользователь с указанным номером не найден')

# Получаем значение среднего возраста пользователей в группе
average_age = (user_list[0]['age'] + user_list[1]['age'] + user_list[2]['age'] + user_list[3]['age']) / len(user_list)
print(f'Средний возраст юзеров составляет {average_age} года')