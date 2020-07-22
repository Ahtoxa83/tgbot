import datetime as time

import psycopg2

f = open('password.txt', 'r')
password = f.read()


print("Проверка забаненых аккаунтов...")
connect = connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
cur = connect.cursor()
cur.execute("SELECT Count(ID) FROM Bots")
all_ids = int(cur.fetchone()[0])
if all_ids != 0:
    print(f"Bots count {all_ids}")
    cur.execute("SELECT ID FROM Bots ORDER BY ID ASC LIMIT 1")
    x = cur.fetchone()[0]
    all_ids = x + all_ids
    while int(x) < int(all_ids):
        cur.execute(f"SELECT IsBanned FROM Bots WHERE ID = {x}")
        if bool(cur.fetchone()[0]) is False:
            print(f"Bot ID{x} не забанен...")
        else:
            print(f"Bot ID {x} забанен. Перевожу аккаунт в таблицу банов...")
            cur.execute(f"SELECT Telephone FROM Bots WHERE ID = {x}")
            telephone = cur.fetchone()[0]
            cur.execute(f"SELECT Password FROM Bots WHERE ID = {x}")
            password = cur.fetchone()[0]
            cur.execute("""INSERT INTO BannedBots(Telephone, Password, BanDate) VALUES(?, ?, ?);""",
                        (telephone, password, time.datetime.today()))

            connect.commit()
            cur.execute(f"DELETE FROM Bots WHERE ID = {x}")
            connect.commit()
            print("Перевод завершен")
        x = x + 1

connect = connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')
cur = connect.cursor()
cur.execute("SELECT Count(ID) FROM RegistredBots")
all_ids = int(cur.fetchone()[0])
if all_ids != 0:
    print(f"Bots count {all_ids}")
    cur.execute("SELECT ID FROM RegistredBots ORDER BY ID ASC LIMIT 1")
    x = cur.fetchone()[0]
    all_ids = x + all_ids
    while int(x) < int(all_ids):
        cur.execute(f"SELECT IsBanned FROM RegistredBots WHERE ID = {x}")
        if bool(cur.fetchone()[0]) is False:
            print(f"Bot ID{x} не забанен...")
        else:
            print(f"Bot ID {x} забанен. Перевожу аккаунт в таблицу банов...")
            cur.execute(f"SELECT Telephone FROM RegistredBots WHERE ID = {x}")
            telephone = cur.fetchone()[0]
            cur.execute(f"SELECT Password FROM RegistredBots WHERE ID = {x}")
            password = cur.fetchone()[0]
            cur.execute("""INSERT INTO BannedBots(Telephone, Password, BanDate) VALUES(?, ?, ?);""",
                        (telephone, password, time.datetime.today()))

            connect.commit()
            cur.execute(f"DELETE FROM RegistredBots WHERE ID = {x}")
            connect.commit()
            print("Перевод завершен")
        x = x + 1