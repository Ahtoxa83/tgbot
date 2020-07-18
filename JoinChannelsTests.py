import psycopg2
import time
from telethon import TelegramClient
import re
import asyncio
import datetime
import sqlite3 as sqlite
from threading import Thread
import random
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon import errors
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest

print(f"Готов вкалывать")
#playsound('readytowork.mp3')
#time.sleep(1)


async def workThread(x):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                        password='s56u9555', host='localhost')
    cur = connect.cursor()
    cur.execute(f"SELECT API_ID FROM RegistredBots WHERE ID = {x}")
    Api_id = cur.fetchone()[0]
    await asyncio.sleep(random.uniform(0.1, 0.5))
    cur.execute(f"SELECT API_HASH FROM RegistredBots WHERE ID = {x}")
    Api_hash = cur.fetchone()[0]
    await asyncio.sleep(random.uniform(0.1, 0.5))
    cur.execute(f"SELECT Session FROM RegistredBots WHERE ID = {x}")
    await asyncio.sleep(random.uniform(0.1, 0.5))
    cur.execute(f"SELECT Session FROM RegistredBots WHERE ID = {x}")
    Session = cur.fetchone()[0]
    print("ТЕСТ 3 задание")
    connect.close()
    client = TelegramClient(Session, Api_id, Api_hash)

    print(f"Пора облопошить этих пидоров")
    await client.start()
    new_file_content = ""
    print(f"Успешный вход в аккаунт - bot id - {x}")
    sorry_count = 0
    count = 0
    max_count = 2
    error_count = 0
    not_free_found = False
    while True:


        if count == max_count:
            print("Хватит этих ебаных групп")
            break
        if sorry_count == 5:
            print("Хватит извинятся ебучий бот")

        if error_count == 5:
            print("Ебаные ошибки")
            break
        try:
            dialogs = await client.get_dialogs()
            for dialog in dialogs:
                if dialog.title == 'LTC Click Bot':
                    thisdialog = dialog
                    print(thisdialog.title)
            await client.send_message('LTC Click Bot', '📣 Join chats')
            time.sleep(2)
            msgs = await client.get_messages(thisdialog, limit=1)
            for mes in msgs:
                if re.search(r"\bSorry\b", mes.message):
                    print("Пидоры извиняются")
                    sorry_count += 1
                entity = mes.reply_markup.rows[0].buttons[0].url
                agree = mes.reply_markup.rows[0].buttons[1].data
                message_id = mes.id
                time.sleep(3)
            print(entity)
        except errors.FloodWaitError as e:
            print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
            time.sleep(e.seconds)



        try:
            await client(JoinChannelRequest(entity))
            print(entity)
            channel_name = entity
        except errors.ChannelsTooMuchError:
            print("Нету свободного места. Проверка доступности выхода с одного из каналов")
            error_count += 1
            connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                       password='s56u9555', host='localhost')
            cur = connect.cursor()
            cur.execute(f"SELECT id,channel, leave_time FROM channel_entity WHERE bot_id = {x}")
            all_channels = cur.fetchall()
            for channel in all_channels:
                if channel[2] < datetime.datetime.now():
                    print(f"Да {channel[0]}/ {channel[1]} /{channel[2]}  < {datetime.datetime.now()}")
                    try:
                        await client(LeaveChannelRequest(channel[1]))
                    except errors.FloodWaitError as e:
                        print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
                        time.sleep(e.seconds)
                    finally:
                        not_free_found = False
                        cur.execute(f"DELETE FROM channel_entity WHERE id = {channel[0]}")
                        connect.commit()
                        break

                else:
                    not_free_found = True
                    print(f"Нет {channel[0]}/ {channel[1]} /{channel[2]}  > {datetime.datetime.now()}")
            connect.close()
        except errors.FloodWaitError as e:
            print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
            time.sleep(e.seconds)
        if not_free_found is True:
            print("Свободного места для канала не найдено...")
            break
        time.sleep(2)
        await client(GetBotCallbackAnswerRequest(
            thisdialog,
            message_id,
            data=agree
        ))
        time.sleep(3)
        msgs = await client.get_messages(thisdialog, limit=2)
        for mes2 in msgs:
            if re.search("Success!", mes2.message):
                waitin = str(mes2.message).replace("Success! 👍\nYou must stay in the channel for at least ", "")
                waitin = str(waitin).replace("Success! 👍\nYou must stay in the group for at least ", "")
                if re.search(" hour to earn your reward.", waitin):
                    waitin = str(waitin).replace(" hour to earn your reward.", "")
                else:
                    waitin = str(waitin).replace(" hours to earn your reward.", "")

                print(f"Ждать {waitin} часа. Да и похуй го некст...")
                print(waitin)
                hours = waitin
                current_date_and_time = datetime.datetime.now()
                hours_added = datetime.timedelta(hours=int(hours))
                future_date_and_time = current_date_and_time + hours_added
                connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                           password='s56u9555', host='localhost')
                cur = connect.cursor()
                cur.execute(f"INSERT INTO channel_entity(channel, join_time, leave_time, bot_id) "
                            f"VALUES ('{entity}', '{current_date_and_time}', '{future_date_and_time}', {x})")
                connect.commit()
                connect.close()
                time.sleep(3)




        time.sleep(3)
        print("Последняя проверка")
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password='s56u9555', host='localhost')
        cur = connect.cursor()
        cur.execute(f"SELECT id,channel, leave_time FROM channel_entity WHERE bot_id = {x}")
        all_channels = cur.fetchall()
        for channel in all_channels:
            if channel[2] < datetime.datetime.now():
                print(f"Удаляем из базы данных т.к. время уже пройдено"
                      f" {channel[0]}/{channel[1]}/{channel[2]}  < {datetime.datetime.now()}")
                try:
                    await client(LeaveChannelRequest(channel[1]))
                except errors.FloodWaitError as e:
                    print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
                    time.sleep(e.seconds)

                finally:
                    cur.execute(f"DELETE FROM channel_entity WHERE id = {channel[0]}")
                    connect.commit()
                    break


        else:
            print(f"Нет {channel[0]}/ {channel[1]} /{channel[2]}  > {datetime.datetime.now()}")


        connect.close()
        count += 1
        print("Выполнено...")







def wrap(i):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio.run(workThread(i))
    loop.close()






if __name__ == '__main__':
    connect5 = sqlite.Connection("ParsedAccounts.db")
    cur1 = connect5.cursor()
    cur1.execute("SELECT Count(ID) FROM RegistredBots")

    nums = cur1.fetchone()[0]
    connect5.close()
    p = []
    for i in range(1, nums + 1):
        p1 = Thread(target=wrap, args=(i,)).start()





#TODO Отформатировать код.
