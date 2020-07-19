import asyncio
import re
import time

import psycopg2
from telethon import TelegramClient
from telethon import errors


async def checks():
    sumofbalance = 0.00
    withdraw = 0.00
    connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                               password='xxxx', host='localhost')
    cur1 = connect.cursor()
    cur1.execute("SELECT ID FROM RegistredBots")
    max = cur1.fetchall()
    connect.close()

    for s in max:
        for i in s:
            connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                       password='xxxxx', host='localhost')
            cur1 = connect.cursor()
            print(f"Проверка баланса у бота ID:{int(i)}")
            cur1.execute(f"SELECT API_ID FROM RegistredBots WHERE ID = {i}")
            Api_id = cur1.fetchone()[0]
            time.sleep(0.5)
            cur1.execute(f"SELECT API_HASH FROM RegistredBots WHERE ID = {i}")
            Api_hash = cur1.fetchone()[0]
            time.sleep(0.5)
            cur1.execute(f"SELECT Session FROM RegistredBots WHERE ID = {i}")
            Session = cur1.fetchone()[0]
            connect.close()
            client = TelegramClient(Session, Api_id, Api_hash)
            await client.start()
            print(f"Успешный вход в аккаунт bot id - {i}")
            print(f"Проверка баланса")
            try:
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    if dialog.title == 'LTC Click Bot':
                        thisdialog = dialog
                        print(thisdialog.title)
                await client.send_message('LTC Click Bot', '💰 Balance')
                time.sleep(3)
                msgs = await client.get_messages(thisdialog, limit=5)
                for mes in msgs:
                    if re.search(r'Available balance: ', mes.message):
                        money = str(mes.message).replace('Available balance: ', '')
                        money1 = str(money).replace(' LTC', '')
                        print(f"Баланс: {str(money1)}")
                        if str(money1) > str(0.0004):
                            print(f"{str(money1)}>{str(0.0004)}")
                            print("Баланс больше 0.0004 произвожу вывод...")
                            await client.send_message('LTC Click Bot', '💵 Withdraw')
                            time.sleep(1)
                            connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                       password='xxxxx', host='localhost')
                            cur1 = connect.cursor()
                            time.sleep(1)
                            cur1.execute(f"SELECT Wallet_Id FROM RegistredBots WHERE ID = {i}")
                            wallet_id = cur1.fetchone()[0]
                            cur1.execute(f"SELECT Wallet_ID FROM Wallets WHERE ID = {wallet_id}")
                            wallet_id = cur1.fetchone()[0]
                            connect.close()
                            time.sleep(1)
                            await client.send_message('LTC Click Bot', str(wallet_id))
                            time.sleep(1)
                            await client.send_message('LTC Click Bot', money1)
                            time.sleep(1)
                            await client.send_message('LTC Click Bot', '✅ Confirm')
                            time.sleep(1)
                            print("Успешный вывод")
                            time.sleep(1)
                            withdraw += float(money1)
                        else:
                            sumofbalance += float(money1)
                        time.sleep(3)
            except errors.FloodWaitError as e:
                print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
                time.sleep(e.seconds)



    print(f"Общий баланс после вывода: {str(sumofbalance)}")
    print(f"Вывод: {withdraw}")


    time.sleep(5)


async def main():
    await checks()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        print('')



#TODO Отформатировать код.

