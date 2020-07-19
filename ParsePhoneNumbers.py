import datetime as time
from os import system, name

import psycopg2


def error_controller(error):
    connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                               password='xxxx', host='localhost')
    cur = connect.cursor()
    cur.execute(f"""Insert Into Errors(Error, Date) VALUES (?, ?);""", (error, time.datetime.today()))
    connect.commit()

def add_new_bots(telephone, password):
    try:
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password='xxxx', host='localhost')
        cur = connect.cursor()
        cur.execute("""Insert Into Bots(Telephone, Password, AddDate) VALUES (?, ?, ?);""",
                    (telephone, password, time.datetime.today()))
        connect.commit()
    except Exception as e:
        print(f"Ошибка {str(e)}. Вношу ошибку в базу данных...")
        error = f"Ошибка {str(e)} при добавлении ботов."
        error_controller(error)
        print(f"Ошибка внесена в базу данных.")


def check_bots():
    try:
        big_result = ""
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password='xxxx', host='localhost')
        cur = connect.cursor()
        cur.execute("SELECT Count(ID) FROM Bots")
        all_ids = int(cur.fetchone()[0])
        if all_ids != 0:
            print(f"Bots count {all_ids}")
            cur.execute("SELECT ID FROM Bots ORDER BY ID ASC LIMIT 1")
            x = cur.fetchone()[0]
            all_ids = x + all_ids
            while int(x) <= int(all_ids):
                try:
                    cur.execute(f"SELECT Telephone FROM Bots WHERE ID = {x}")
                    res = cur.fetchone()[0]
                    if res is not None:
                        big_result += f"Bot id {x} telephone {res}\n"

                    x = x + 1
                except Exception as e:
                    print(f"Ошибка {str(e)} in bot ID {x}. Вношу ошибку в базу данных...")
                    error = f"Ошибка {str(e)} int bot ID {x} при проверке ботов."
                    error_controller(error)
                    print(f"Ошибка внесена в базу данных.")
                    x = x + 1
            print(f"Все боты:\n{big_result}")
        else:
            print("В базе данных нет ботов")
    except Exception as e:
        print(f"Ошибка {str(e)}. Вношу ошибку в базу данных...")
        error = f"Ошибка {str(e)} при проверке ботов."
        error_controller(error)
        print(f"Ошибка внесена в базу данных.")




def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while True:
    clear()
    print("1.Добавить новый аккаунт")
    print("2.Просмотреть базу данных")
    input_num = input()
    if input_num == str(1):
        print("Введите телефон")
        tel = input()
        print("Введите пароль")
        pas = input()
        add_new_bots(tel, pas)
    elif input_num == str(2):
        print("Проверка всех ботов")
        check_bots()
    else:
        break
