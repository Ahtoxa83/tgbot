import asyncio
import random
import re
import time
from threading import Thread

import psycopg2
from telethon import TelegramClient
from telethon import errors
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from telethon.tl.functions.users import GetFullUserRequest

print(f"Готов вкалывать")
#playsound('readytowork.mp3')
#time.sleep(1)


async def workThread(x):
    exit = False
    await asyncio.sleep(random.uniform(0.1, 0.5))
    print(f"MultiThreadForBotID: {x}")
    while True:
        if exit is True:
            print("Выполнение заданий 2 окончено")
            break
        not_message = 0
        count_tryes = 0
        wait_in_quests = 0
        max_count_types = 3

        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password='s56u9555', host='localhost')
        cur = connect.cursor()
        cur.execute(f"SELECT API_ID FROM RegistredBots WHERE ID = {x}")
        Api_id = cur.fetchone()[0]
        time.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT API_HASH FROM RegistredBots WHERE ID = {x}")
        Api_hash = cur.fetchone()[0]
        time.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT Session FROM RegistredBots WHERE ID = {x}")
        time.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT Session FROM RegistredBots WHERE ID = {x}")
        Session = cur.fetchone()[0]
        connect.close()
        print(f"Приступаем к заданиям на переписку с ботами BOT ID{x}")
        client = TelegramClient(Session, Api_id, Api_hash)
        await client.start()
        print(f"Успешный вход в аккаунт - bot id - {x}")
        print(f"Пора облопошить этих пидоров")
        while True:
            next = True
            if not_message == 3:
                print(f"Ботяр этих еблан писал ей богу хули они молчат")
                exit = True
                break
            if count_tryes == max_count_types:
                print(f"Повыполняли этих гавнокоденных заданий и хватит")
                exit = True
                break
            if wait_in_quests == 5:
                print(f"Гавнокоденных заданий нет. Печалька а то так много давали")
                exit = True
                break
            try:
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    if dialog.title == 'LTC Click Bot':
                        thisdialog = dialog
                        print(thisdialog.title)
                await client.send_message('LTC Click Bot', '🤖 Message bots')
                time.sleep(2)
                msgs = await client.get_messages(thisdialog, limit=1)
                for mes in msgs:
                    if re.search(r'\bSorry\b', mes.message):
                        print("Пидоры извиняются")
                        wait_in_quests += 1
                        print("Ниче еще раз проверим")

                        next = False
                    else:
                        entity = mes.reply_markup.rows[0].buttons[0].url
                        message_id = mes.id
                        reqdata = mes.reply_markup.rows[1].buttons[1].data
                        time.sleep(3)

                    if next is True:
                        print(entity)
                        entity = str(entity).replace("https://t.me/", "")
                        entity = str(entity).split("?")[0]

                        full = await client(GetFullUserRequest(entity))
                        bot = full.user
                        if bot.last_name is None:
                            full_bot_entity = bot.first_name
                        else:
                            full_bot_entity = str(f"{bot.first_name} {bot.last_name}")

                        print(entity)
                        await client.send_message(entity, '/start')

                        time.sleep(5)
                        for dialog in dialogs:
                            if dialog.title == full_bot_entity:
                                thisdialog1 = dialog
                                print(thisdialog1.title)
                        msgs2 = await client.get_messages(thisdialog1, limit=1)
                        for mes2 in msgs2:
                            if mes2 is None:
                                print("Уебки на ботяре")
                                await client(GetBotCallbackAnswerRequest(
                                    thisdialog,
                                    message_id,
                                    data=reqdata
                                ))
                                print("Скипаем уебского бота")
                                not_message += 1
                            elif mes2.message == "/start":
                                print("Уебки на ботяре не пишет нихуя /start отправлять не буду")
                                await client(GetBotCallbackAnswerRequest(
                                    thisdialog,
                                    message_id,
                                    data=reqdata
                                ))
                                print("Скипаем уебского бота")
                                not_message += 1
                            else:
                                await client.forward_messages('LTC Click Bot', mes2.id, entity)
                                print(f"БОТ {x} ПОГОВОРИЛ С БОТОМ И ПОЛУЧИЛ КЭШ")
                                count_tryes += 1

            except errors.FloodWaitError as e:
                print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
                time.sleep(e.seconds)



def wrap(i):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio.run(workThread(i))
    loop.close()


if __name__ == '__main__':
    connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                               password='s56u9555', host='localhost')
    cur1 = connect.cursor()
    cur1.execute("SELECT Count(ID) FROM RegistredBots")

    nums = cur1.fetchone()[0]
    connect.close()
    p = []
    for i in range(1, nums + 1):
        p1 = Thread(target=wrap, args=(i,)).start()


#TODO Отформатировать код.
#TODO Переписать вывод в потоки. Переписать строку запроса для потоков SELECT Count(ID) FROM RegistredBots на SELECT ID FROM RegistredBots для того чтобы исправить ошибку