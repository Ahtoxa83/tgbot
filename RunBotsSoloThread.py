import asyncio
import random
import re
import time
import urllib.request

import psycopg2
from telethon import TelegramClient
from telethon import errors
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

f = open('password.txt', 'r')
password = f.read()

async def workThread(x):
    await asyncio.sleep(random.uniform(0.1, 0.5))

    print(f"SoloThreadForBotID: {x}")
    exit_pool = False
    while True:

        if exit_pool is True:
            break
        connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                                   password=password, host='localhost')

        cur = connect.cursor()
        cur.execute(f"SELECT API_ID FROM RegistredBots WHERE ID = {x}")
        Api_id = cur.fetchone()[0]
        await asyncio.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT API_HASH FROM RegistredBots WHERE ID = {x}")
        Api_hash = cur.fetchone()[0]
        await asyncio.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT Session FROM RegistredBots WHERE ID = {x}")
        Session = cur.fetchone()[0]
        await asyncio.sleep(random.uniform(0.1, 0.5))
        cur.execute(f"SELECT Phone FROM RegistredBots WHERE ID = {x}")
        Phone = cur.fetchone()[0]
        await asyncio.sleep(random.uniform(0.1, 0.5))
        print(f"Попытка входа в аккаунт - {Phone} bot id - {x}")
        await asyncio.sleep(random.uniform(1, 2))
        connect.close()
        client = TelegramClient(Session, Api_id, Api_hash)
        await client.start()
        print(f"Успешный вход в аккаунт - {Phone} bot id - {x}")
        print(f"Пора облопошить этих пидоров")
        capcha_counts = 0
        wait_in_quests = 0
        count_tryes = 0
        max_count_types = 3
        errors_count = 0
        errors_bool = False
        thisdialog = None
        while True:
            capcha = False
            if capcha_counts == 10:
                print("Пидоры оказались сильнее")
                print(f"Отступаемcapcha БОТОМ ID-{x}")
                connect.close()
                exit_pool = True
                break
            if wait_in_quests == 3:
                print("Ну и бомжи ебаные нету даже заданий")
                print(f"Отступаемwaitin БОТОМ ID-{x}")
                connect.close()
                exit_pool = True
                x += 1
                break
            if count_tryes == max_count_types:
                print("Ну пару раз выполнил и хватит")
                print(f"Отступаемtryes БОТОМ ID-{x}")
                connect.close()
                exit_pool = True
                break
            if errors_count == 10:
                print("Что то пошло по пизде")
                print(f"Отступаемerror БОТОМ ID-{x}")
                connect.close()
                exit_pool = True
                break
            try:
                dialogs = await client.get_dialogs()
                for dialog in dialogs:
                    if dialog.title == 'LTC Click Bot':
                        thisdialog = dialog
                        print(thisdialog.title)

                await client.send_message('LTC Click Bot', '🖥 Visit sites')
                time.sleep(5)
                msgs = await client.get_messages(thisdialog, limit=1)
                for mes in msgs:
                    if re.search(r'Press the "Visit website"', mes.message):
                        button_data = mes.reply_markup.rows[1].buttons[1].data
                        message_id = mes.id
                        time.sleep(3)

                    elif re.search(r'\bSorry\b', mes.message):
                        print("Пидоры извиняются")
                        wait_in_quests += 1
                        print("Ниче еще раз проверим")
                        errors_bool = True

                    elif re.search(r'\bThe address you entered looks invalid.\b', mes.message):
                        print("Ошибка после проверки баланса. Исправляем...")
                        await client.send_message('LTC Click Bot', '❌ Cancel')
                        errors_bool = True

                time.sleep(2)
                if errors_bool is False:
                    print(f"Идет переход по ссылке {msgs[0].reply_markup.rows[0].buttons[0].url}")
                    url_rec = msgs[0].reply_markup.rows[0].buttons[0].url
                    tryes = 0
                    goods = False
                    while True:
                        try:
                            if goods is True:
                                print(f"ВСЕ ЗАЕБУМБА БОТОМ ID-{x}")
                                break
                            if (tryes > 5):
                                print(f"Неудачно БОТОМ ID-{x}")
                                capcha = True
                                break
                            fp = urllib.request.urlopen(url_rec)
                            print(f"Открывает БОТОМ ID-{x}")
                            mybytes = fp.read()
                            print(f"Читает БОТОМ ID-{x}")
                            time.sleep(2)
                            mystr = mybytes.decode("utf8")
                            print(f"Декодит БОТОМ ID-{x}")
                            time.sleep(2)
                            fp.close()
                            print(f"Закрывает БОТОМ ID-{x}")
                            time.sleep(2)
                            msgs = await client.get_messages(thisdialog, limit=1)
                            for mes7 in msgs:
                                if re.search(r'You must stay on the site for ', mes7.message):
                                    wait_time = str(mes7.message).replace('You must stay on the site for', '')
                                    wait_time = str(wait_time).replace('seconds to get your reward.', '')
                                    str_wait = int(wait_time) + 5
                                    print(f"Сидим пердим {str(str_wait)} секунд")
                                    time.sleep(int(wait_time) + 5)
                                    goods = True
                                    break

                                elif re.search(r'Please stay on the site for at least ', mes7.message):
                                    wait_time = str(mes7.message).replace('Please stay on the site for at least ', '')
                                    wait_time = str(wait_time).replace(' seconds...', '')
                                    str_wait = int(wait_time) + 5
                                    print(f"Сидим пердим {str(str_wait)} секунд")
                                    time.sleep(int(wait_time) + 5)
                                    goods = True
                                    break
                            if re.search(r'\breCAPTCHA\b', mystr):
                                time.sleep(2)
                                print(f"ПИДОРЫ DETECTED! БОТОМ ID-{x}")
                                capcha = True
                                break


                            else:
                                time.sleep(3)
                                msgs = await client.get_messages(thisdialog, limit=1)
                                for mes3 in msgs:
                                    if re.search(r'You must stay on the site for ', mes3.message):
                                        wait_time = str(mes3.message).replace('You must stay on the site for', '')
                                        wait_time = str(wait_time).replace('seconds to get your reward.', '')
                                        str_wait = int(wait_time) + 5
                                        print(f"Сидим пердим {str(str_wait)} секунд БОТОМ ID-{x}")
                                        time.sleep(int(wait_time) + 5)
                                        goods = True
                                        break

                                    elif re.search(r'Please stay on the site for at least ', mes3.message):
                                        wait_time = str(mes3.message).replace(
                                            'Please stay on the site for at least ',
                                            '')
                                        wait_time = str(wait_time).replace(' seconds...', '')
                                        str_wait = int(wait_time) + 5
                                        print(f"Сидим пердим {str(str_wait)} секунд БОТОМ ID-{x}")
                                        time.sleep(int(wait_time) + 5)
                                        goods = True
                                        break

                                break
                        except Exception as er:
                            print(f"Смотрим БОТОМ ID-{x}")
                            wait_time = 0

                            msgs1 = await client.get_messages(thisdialog, limit=1)
                            for mes6 in msgs1:
                                print(mes6.message)
                                if re.search(r'You must stay on the site for ', mes6.message):
                                    wait_time = str(mes6.message).replace('You must stay on the site for', '')
                                    wait_time = str(wait_time).replace('seconds to get your reward.', '')
                                    str_wait = int(wait_time) + 5
                                    print(f"Сидим пердим {str(str_wait)} секунд")
                                    goods = True
                                    time.sleep(int(wait_time) + 5)
                                    break

                                elif re.search(r'Please stay on the site for at least ', mes6.message):
                                    wait_time = str(mes6.message).replace('Please stay on the site for at least ', '')
                                    wait_time = str(wait_time).replace(' seconds...', '')
                                    str_wait = int(wait_time) + 5
                                    print(f"Сидим пердим {str(str_wait)} секунд БОТОМ ID-{x}")
                                    goods = True
                                    time.sleep(int(wait_time) + 5)
                                    break
                                elif re.search(r'\bSorry\b', mes.message):
                                    print("Пидоры извиняются")
                                    wait_in_quests += 1
                                    print("Ниче еще раз проверим")
                                    capcha = True
                                else:
                                    print(f"Ошибка входа {er}. Пробую еще раз БОТОМ ID-{x}")
                                    tryes += 1
                                    time.sleep(1)

                if capcha is True:
                    print("Пробуем еще раз...")
                    msgs5 = await client.get_messages(thisdialog, limit=15)
                    for mes16 in msgs5:
                        if re.search(r'Press the "Visit website"', mes16.message):
                            await client(GetBotCallbackAnswerRequest(
                                thisdialog,
                                mes16.id,
                                data=mes16.reply_markup.rows[1].buttons[1].data
                            ))
                            time.sleep(1)
                            print(f"Скипаем хуйню БОТОМ ID-{x}")
                            break
                    capcha_counts += 1
                else:
                    stranger = False
                    time.sleep(0.2)
                    money_earned = ""
                    money_earned_float = 0.000000000000
                    msgs = await client.get_messages(thisdialog, limit=15)
                    for mes88 in msgs:
                        if re.search(r'You earned ', mes88.message):
                            money_earned = str(mes88.message).replace('You earned ', '')
                            money_earned_float = float(str(money_earned).replace(' LTC for visiting a site!', ''))
                            print(f"Бля хуйня ккая то {str(money_earned).replace(' LTC for visiting a site!', '')}")

                            break

                    print(f"Заработано: " + str(money_earned_float) + "LTC")
                    if round(money_earned_float, 6) == 0.000000:
                        print("Скипаем какую то неведомую пока что дичь")
                        msgs888 = await client.get_messages(thisdialog, limit=15)
                        for mes166 in msgs888:
                            if re.search(r'Press the "Visit website"', mes166.message):
                                await client(GetBotCallbackAnswerRequest(
                                    thisdialog,
                                    mes166.id,
                                    data=mes166.reply_markup.rows[1].buttons[1].data
                                ))
                                time.sleep(1)
                                break
                        capcha_counts += 1
                        stranger = True

                    if stranger is False:
                        # connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                        #                                password=password, host='localhost')
                        # cur = connect.cursor()
                        # cur.execute(f"SELECT LTC_Earned FROM RegistredBots WHERE ID = {x}")
                        await asyncio.sleep(random.uniform(0.1 + x, 0.5 + x))
                        # full_ltc = cur.fetchone()[0]
                        await asyncio.sleep(random.uniform(0.1 + x, 0.5 + x))
                        # print(f"ВСЕГО ЗАРАБОТАНО БОТОМ ID-{x} MONEY:{str(full_ltc)}")
                        await asyncio.sleep(random.uniform(0.1 + x, 0.5 + x))
                        # cur.execute(
                        #    f"UPDATE RegistredBots SET LTC_Earned = {float(full_ltc) + float(money_earned_float)} WHERE ID = {x}")
                        # connect.commit()
                        # connect.close()
                        await asyncio.sleep(random.uniform(0.1 + x, 0.7 + x))
                        count_tryes += 1
                        print(f"Давай еще {str(max_count_types - count_tryes)} разочка(ов) по-выполняем...")

            except errors.FloodWaitError as e:
                print(f'Нас опракинули ебалом в грязь сидим {e.seconds} секунд')
                time.sleep(e.seconds)


def wrap(i):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio.run(workThread(i))
    loop.close()


def main():
    print("Пизда им")


if __name__ == '__main__':
    connect = psycopg2.connect(dbname='parsedaccounts', user='postgres',
                               password=password, host='localhost')
    cur1 = connect.cursor()
    cur1.execute("SELECT ID FROM RegistredBots")

    nums = cur1.fetchall()
    for num in nums:
        wrap(num[0])







