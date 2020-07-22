from os import system, name

import psycopg2
from telethon import TelegramClient


def clear():
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

f = open('password.txt', 'r')
password = f.read()

def find_bot(telephone):
    try:
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
        cur = connect.cursor()
        cur.execute(f"SELECT ID FROM Bots WHERE Telephone = '{telephone}'")
        ids = cur.fetchone()[0]
        if ids is not None:
            return ids
        else:
            return -1
    except Exception as e:
        print(f"Ошибка {str(e)}.")


def add_new_bots(telephone, api_id, api_hash, session):
    try:
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
        cur = connect.cursor()
        cur.execute(f"Insert Into RegistredBots(Phone, API_ID, API_HASH, Session) VALUES ('{telephone}', '{api_id}', '{api_hash}', '{session}')")

        connect.commit()
        cur.execute(f"DELETE FROM Bots WHERE Telephone = '{telephone}'")
        connect.commit()
        print("Аккаунт перемещен в таблицу RegistredBots")
    except Exception as e:
        print(f"Ошибка {str(e)}.")



print("Введите телефон: ")
telephone = input()
print("Введите API_ID: ")
api_id = input()
print("Введите API_HASH: ")
api_hash = input()
id = find_bot(telephone)
if id != -1:
    while True:
        i = 0
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
        cur = connect.cursor()
        session = f"anon{id+i}"
        try:
            cur.execute(f"SELECT Session FROM RegistredBots WHERE Session = '{session}'")
            sess_name = cur.fetchone()
            if sess_name is not None:
                print(f"Сессия anon{id + i} уже существует")
                i += 1
            else:
                break
        except Exception as e:
            print("")





    client = TelegramClient(session, api_id, api_hash)
    client.start()
    print("Успешно!")
    add_new_bots(telephone, api_id, api_hash, session)
else:
    print("Телефон не найдет в таблице Bots")

#TODO Отформатировать код.
