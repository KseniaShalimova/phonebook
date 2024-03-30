import json

def save_js():
    with open('tel.json', 'w', encoding='utf-8') as write_file:
        json.dump(phonebook, write_file, ensure_ascii=False)

def load_js():
    with open('tel.json', 'r', encoding='utf-8') as read_file:
        ph = json.load(read_file)
    print('Телефонная книга успешно загружена!')

def find_or_del(parameter,key):
    unfulfilled = True
    for i in phonebook:
        for u in phonebook[i][parameter]:
            if u == key:
                contact = i
                unfulfilled = False
    return contact, phonebook[contact], unfulfilled

def find():
    contact, found, unfulfilled = find_or_del(parameter, key)
    if unfulfilled:
        print('В телефонной книге нет контакта с такими данными!')
    else:
        print('Результаты поиска:')
        print(f'"{contact}": {phonebook[contact]}')

def delete(message):
    contact, found, unfulfilled = find_or_del(parameter, key)
    try:
        found[parameter].remove(key)
        print(f'{message} {key} успешно удален(-а)')
    except:
        print('В телефонной книге нет контакта с такими данными!')

def add_phone_or_email(message1, message2, message3, parameter): # почту, почта, одну почту
    key = input(f'Введите {message1}: ')
    name = input('Введите имя контакта, к которому необходимо добавить: ')
    try:
        if key!='':
            phonebook[name][parameter].append(key)
            print(f'{message2} успешно добавлен(-а)')
            while True:
                if input(f'Добавить ещё {message3}?(Введите yes/no): ').lower() == 'yes':
                    key = input(f'Введите {message1}: ')
                    phonebook[name][parameter].append(key)
                    print(f'{message2} успешно добавлен(-а)')
                else:
                    break
    except:
        print('Такого контакта в телефонной книге нет')


try:
    with open('tel.json', 'r', encoding='utf-8') as read_file:
        phonebook = json.load(read_file)
    print('Телефонная книга успешно загружена!')
except:
    phonebook = {
    "дядя Ваня": {"phones": ["+7123", "321"],
                  "birthday": ["01.01.1960"],
                  "email": ["vanya@mail.ru", "vanechka@mail.ru"]},
    "дядя Вася": {"phones": ["222", "+7333"],
                  "birthday": ["04.01.1998"],
                  "email": ["vasya@mail.ru"]}
                }

print('''
      Добро пожаловать в телефонную книгу!
      Чтобы увидеть список команд - введите /help
      ''')

while True:
    command=input('Введите команду: ')

    if command == '/stop':
        save_js()
        print('Телефонная книга закрыта')
        break

    elif command == '/help':
        print('''
              Список команд:
              /help - список всех команд
              /stop - закрыть телефонную книгу
              /all - показать все контакты
              /find - найти контакт по одному из параметров: имя, телефон, дата рождения, почта
              /save - сохранить изменения(сохраняются автоматичеки при закрытии телефонной книги)
              /load - загрузить телефонную книгу
              /del - удалить отдельный параметр или целый контакт
              /add - добавить отдельный параметр или целый контакт
              ''')

    elif command == '/all':
        print("Текущие записи в телефонной книге:")
        print(phonebook)
    
    elif command == '/save':
        save_js()
        print('Изменения в телефонной книге успешно сохранены!')
    
    elif command == '/load':
        load_js()
    
    elif command == '/find':
        parameter = input("По какому параметру ведётся поиск (Введите 'name' - если по имени, 'phones' - если по номеру телефона, 'birthday' - если по дате рождения, 'email' - если по почте): ")
        if parameter == 'name':
            key = input('Введите имя: ')
            try:
                print('Результаты поиска:')
                print(f'"{key}": {phonebook[key]}')
            except:
                print('В телефонной книге нет контакта с такими данными!')
        
        elif parameter == 'phones':
            key = input('Введите номер телефона: ')
            find()
        
        elif parameter == 'birthday':
            key = input('Введите дату рождения: ')
            find()
        
        elif parameter == 'email':
            key = input('Введите почту: ')
            find()
        
        else:
            print('В телефонной книге не хранятся такие параметры')
    
    elif command == '/del':
        parameter = input("Какой параметр необходимо удалить (Введите 'name' - если полностью контакт, 'phones' - если номер телефона, 'birthday' - если дату рождения, 'email' - если почту): ")
        if parameter == 'name':
            key = input('Введите имя: ')
            phonebook.pop(key)
            print(f'Контакт {key} полностью удален')
        
        elif parameter == 'phones':
            key = input('Введите номер телефона: ')
            message = 'Номер телефона'
            delete(message)
        
        elif parameter == 'birthday':
            key = input('Введите дату рождения: ')
            message = 'Дата рождения'
            delete(message)
        
        elif parameter == 'email':
            key = input('Введите почту: ')
            message = 'Почта'
            delete(message)
        else:
            print('В телефонной книге не хранятся такие параметры')
    
    elif command == '/add':
        parameter = input("Какой параметр необходимо добавить (Введите 'name' - если полностью контакт, 'phones' - если номер телефона, 'birthday' - если дату рождения, 'email' - если почту): ")
        if parameter == 'name':
            name = input('Введите имя контакта: ')
            phonebook[name] = {"phones": [],
                               "birthday": [],
                               "email": []}
            
            phone = input('Введите номер телефона: ')
            if phone!='':
                phonebook[name]["phones"].append(phone)
                print('Номер телефона успешно добавлен')
                while True:
                    if input('Добавить ещё один номер?(Введите yes/no): ').lower() == 'yes':
                        phone = input('Введите номер телефона: ')
                        phonebook[name]["phones"].append(phone)
                        print('Номер телефона успешно добавлен')
                    else:
                        break
            
            birthday = input('Введите дату рождения: ')
            if birthday!= '':
                phonebook[name]["birthday"].append(birthday)
                print('Дата рождения успешно добавлена')
            
            email = input('Введите почту: ')
            if email!= '':
                phonebook[name]["email"].append(email)
                print('Почта успешно добавлена')
                while True:
                    if input('Добавить ещё одну почту?(Введите yes/no): ').lower() == 'yes':
                        phone = input('Введите почту: ')
                        phonebook[name]["email"].append(email)
                        print('Почта успешно добавлена')
                    else:
                        break
            print('Контакт успешно сохранен!')
            print(f'"{name}": {phonebook[name]}')
        
        elif parameter == 'phones':
            add_phone_or_email('номер телефона', 'номер телефона', 'один номер телефона', 'phones')
        
        elif parameter == 'email':
            add_phone_or_email('почту', 'почта', 'одну почту', 'email')
        
        elif parameter == 'birthday':
            birthday = input('Введите дату рождения: ')
            name = input('Введите имя контакта, к которому необходимо добавить: ')
            try:
                if birthday!= '':
                    phonebook[name]["birthday"].append(birthday)
                    print('Дата рождения успешно добавлена')
            except:
                print('Такого контакта в телефонной книге нет')
        else:
            print('В телефонной книге не хранятся такие параметры')
    
    else:
        print('Такой команды нет! Вы можете посмотреть список всех возможных команд, для этого напишите "/help"')