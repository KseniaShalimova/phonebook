import telebot
from random import *
import json

def find_or_del(parameter,key):
    unfulfilled = True
    try:
        for e in phonebook:
            for u in phonebook[e][parameter]:
                if u == key:
                    contact = e
                    unfulfilled = False
        return contact, phonebook[contact], unfulfilled
    except:
        return None, None, unfulfilled

def find(parameter, key):
    contact, found, unfulfilled = find_or_del(parameter, key)
    if unfulfilled:
        text = "В телефонной книге нет контакта с такими данными!"
        # bot.send_message(message.chat.id,"В телефонной книге нет контакта с такими данными!")
    else:
        text = f'''Результаты поиска:
"{contact}": {phonebook[contact]}
        '''
        # bot.send_message(message.chat.id,"Результаты поиска:")
        # bot.send_message(message.chat.id,f'"{contact}": {phonebook[contact]}')
    return text

def delete(message, parameter, key):
    contact, found, unfulfilled = find_or_del(parameter, key)
    try:
        found[parameter].remove(key)
        text = f'{message} {key} успешно удален(-а)'
        # bot.send_message(message.chat.id,f'{message} {key} успешно удален(-а)')
    except:
        text = 'В телефонной книге нет контакта с такими данными!'
        # bot.send_message(message.chat.id,'В телефонной книге нет контакта с такими данными!')
    return text

def add_phone_or_email_or_birth(message2, parameter, key, name_who): # почту, почта, одну почту
    # name = input('Введите "" ')
    try:
        if key!='':
            phonebook[name_who][parameter].append(key)
            text = f'{message2} успешно добавлен(-а)'
            # while True:
            #     if input(f'Добавить ещё {message3}?(Введите yes/no): ').lower() == 'yes':
            #         key = input(f'Введите {message1}: ')
            #         phonebook[name][parameter].append(key)
            #         bot.send_message(message.chat.id,f'{message2} успешно добавлен(-а)')
            #     else:
            #         break
    except:
        text = 'Такого контакта в телефонной книге нет'
    return text

def save_js():
    with open('tel.json', 'w', encoding='utf-8') as write_file:
        json.dump(phonebook, write_file, ensure_ascii=False)

def load_js():
    with open('tel.json', 'r', encoding='utf-8') as read_file:
        phonebook = json.load(read_file)




API_TOKEN = '6861670273:AAHvjR05a_RcU-KltS9keNIiWk9x4sIEutM'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start']) # функция выполняет функцию. Это декоратор
def start_message(message):
    global phonebook
    try:
        with open('tel.json', 'r', encoding='utf-8') as read_file:
            phonebook = json.load(read_file)
        bot.send_message(message.chat.id,"Телефонная книга успешно загружена!")
    except:
        phonebook = {
        "дядя Ваня": {"phones": ["+7123", "321"],
                      "birthday": ["01.01.1960"],
                      "email": ["vanya@mail.ru", "vanechka@mail.ru"]},
        "дядя Вася": {"phones": ["222", "+7333"],
                      "birthday": ["04.01.1998"],
                      "email": ["vasya@mail.ru"]}
                    }
        bot.send_message(message.chat.id,"Не получилось загрузить телефонную книгу")
    bot.send_message(message.chat.id,'''
    Добро пожаловать в телефонную книгу!
Чтобы увидеть список команд - введите /help
      ''')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'''
              Список команд:
/help - список всех команд
/all - показать все контакты
/find - найти контакт по одному из параметров: имя, телефон, дата рождения, почта
/save - сохранить изменения
/load - загрузить телефонную книгу
/del - удалить отдельный параметр или целый контакт
/add - добавить отдельный параметр или целый контакт
''')



@bot.message_handler(commands=['all']) # каждая функция прикреплена к своему декоратору
def show_all(message):
    try:
        bot.send_message(message.chat.id,"Текущие записи в телефонной книге:")
        string = ''
        for i in phonebook:
            string = string + f''' {i}: номера телефонов: {", ".join(phonebook[i]["phones"])}; дата рождения: {", ".join(phonebook[i]["birthday"])}; почта: {", ".join(phonebook[i]["email"])}
'''
        bot.send_message(message.chat.id, string)
    except:
        bot.send_message(message.chat.id, 'Телефонная книга то пустая')



@bot.message_handler(commands=['save'])
def save_all(message):
    save_js()
    bot.send_message(message.chat.id,'Изменения в телефонной книге успешно сохранены!')

@bot.message_handler(commands=['load'])
def load_all(message):
    load_js()
    bot.send_message(message.chat.id,'Телефонная книга успешно загружена!')




@bot.message_handler(commands=['find'])
def find_in_phonebook(message):
    bot.send_message(message.chat.id,'По какому параметру ведётся поиск? Введите название параметра(имя, номер телефона, дата рождения, почта) и сам параметр через пробел. В следующем сообщении введите /find_in')

@bot.message_handler(commands=['find_in'])
def find_in(message):
    if parameter=='name':
        key = inputs
        try:
            bot.send_message(message.chat.id,'Результаты поиска:')
            bot.send_message(message.chat.id,f'"{key}": {phonebook[key]}')
        except:
            bot.send_message(message.chat.id,'В телефонной книге нет контакта с такими данными!')
    elif parameter=='phones':
        key = inputs
        text = find('phones', key)
        bot.send_message(message.chat.id,text)
    elif parameter=='birthday':
        key = inputs
        text = find('birthday', key)
        bot.send_message(message.chat.id,text)
    elif parameter=='email':
        key = inputs
        text = find('email', key)
        bot.send_message(message.chat.id,text)
    else:
        bot.send_message(message.chat.id,'В телефонной книге не хранятся такие параметры')



@bot.message_handler(commands=['del'])
def delete_in_phonebook(message):
    bot.send_message(message.chat.id,'Какой параметр необходимо удалить? Введите название параметра(имя - если полностью контакт, номер телефона, дата рождения, почта) и сам параметр через пробел. В следующем сообщении введите /del_in')


@bot.message_handler(commands=['del_in'])
def del_in(message):
        if parameter=='name':
            key = inputs
            phonebook.pop(key)
            bot.send_message(message.chat.id,f'Контакт {key} полностью удален')
        elif parameter=='phones':
            key = inputs
            msg = 'Номер телефона'
            text = delete(msg, 'phones', key)
            bot.send_message(message.chat.id,text)
        elif parameter=='birthday':
            key = inputs
            msg = 'Дата рождения'
            text = delete(msg, 'birthday', key)
            bot.send_message(message.chat.id,text)
        elif parameter=='email':
            key = inputs
            msg = 'Почта'
            text = delete(msg, 'email', key)
            bot.send_message(message.chat.id,text)
        else:
            bot.send_message(message.chat.id,'В телефонной книге не хранятся такие параметры')
        save_js()
        

@bot.message_handler(commands=['add'])
def add_in_phonebook(message):
    bot.send_message(message.chat.id,'Какой параметр необходимо добавить? Введите название параметра(имя - если полностью контакт, номер телефона, дата рождения, почта) и сам параметр через пробел. В следующем сообщении введите /add_in')

@bot.message_handler(commands=['add_in'])
def add_in(message):
    if parameter=='name':
        name = inputs
        phonebook[name] = {"phones": [],
                               "birthday": [],
                               "email": []}
        bot.send_message(message.chat.id, 'Создан пустой контакт! Вы можете заполнить его самостоятельно :)')
        save_js()
    elif parameter == 'phones':
        bot.send_message(message.chat.id, 'К какому контакту необходимо добавить этот номер? Введите слово "контакт", а затем имя контакта через пробел. В следующем сообщении введите /add_phone')
    elif parameter == 'birthday':
        bot.send_message(message.chat.id, 'К какому контакту необходимо добавить эту дату рождения? Введите слово "контакт", а затем имя контакта через пробел. В следующем сообщении введите /add_birth')
    elif parameter == 'birthday':
        bot.send_message(message.chat.id, 'К какому контакту необходимо добавить эту почту? Введите слово "контакт", а затем имя контакта через пробел. В следующем сообщении введите /add_email')



@bot.message_handler(commands=['add_phone'])
def add_phone(message):
    key = inputs
    text = add_phone_or_email_or_birth('номер телефона', 'phones', key, name_who)
    bot.send_message(message.chat.id,text)
    save_js()

@bot.message_handler(commands=['add_birth'])
def add_birth(message):
    key = inputs
    text = add_phone_or_email_or_birth('дата рождения', 'birthday', key, name_who)
    bot.send_message(message.chat.id,text)
    save_js()

@bot.message_handler(commands=['add_email'])
def add_email(message):
    key = inputs
    text = add_phone_or_email_or_birth('почта', 'email', key, name_who)
    bot.send_message(message.chat.id,text)
    save_js()





@bot.message_handler(content_types=['text']) 
def get_text_message(message):
    global inputs
    global parameter
    global name_who
    if 'имя ' in message.text.lower():
        inputs = message.text[message.text.find('имя ')+5:]
        parameter = 'name'
    elif 'номер телефона ' in message.text.lower():
        inputs = message.text[message.text.find('номер телефона ')+16:]
        parameter = 'phones'
    elif 'дата рождения ' in message.text.lower():
        inputs = message.text[message.text.find('дата рождения ')+15:]
        parameter = 'birthday'
    elif 'почта ' in message.text.lower():
        inputs = message.text[message.text.find('почта ')+7:]
        parameter = 'email'
    elif "контакт " in message.text.lower():
        name_who = message.text[8:]




bot.polling()